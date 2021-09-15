import sys
import math
import copy
import functools
import config
import utils
import overhead_parameter

# Reset "considered" flag on cores
# This is invoked when a new task is selected for scheduling
def reset_considered (cores):
  for c in cores:
    core = cores[c]
    core['considered'] = False

# Implements the first fit bin-packing algorithm
# To use it set config.FIRST_FIT_BP to True
def first_fit_bin_packing (task, cores):
  for c in cores:
    core = cores[c]
    if not core['considered'] and core['utilization'] <= 1:
      return c
  return None

# Implements the first fit bin-packing algorithm
# To use it set config.WORST_FIT_BP to True
def worst_fit_bin_packing (task, cores):
  min_utilization = 1
  result = None
  for c in cores:
    core = cores[c]
    if not core['considered'] and core['utilization'] <= min_utilization and core['utilization'] <= 1:
      result = c
      min_utilization = core['utilization']
  return result


# Implements the best fit bin-packing algorithm
# To use it set config.BEST_FIT_BP to True
def best_fit_bin_packing (task, cores):
  max_utilization = 0
  result = None
  for c in cores:
    core = cores[c]
    # if not core['considered'] and core['utilization'] + task['U'] >= max_utilization and core['utilization'] + task['U'] <= 1:
    if not core['considered'] and core['utilization'] >= max_utilization and core['utilization'] <= 1:
      result = c
      max_utilization = core['utilization']
  return result
  '''  max_utilization = -1
  result = None
  for c in cores:
    core = cores[c]
    # if not core['considered'] and core['utilization'] + task['U'] >= max_utilization and core['utilization'] + task['U'] <= 1:
    new_U = core['utilization'] + task['U']
    if not core['considered'] and new_U > max_utilization and new_U <= 1:
      result = c
      max_utilization = core['utilization']
  return result'''

# Get the next core to check according to the algorithm specified in the config
def get_next_core (task, cores):
  if config.FIRST_FIT_BP:
    return first_fit_bin_packing(task, cores)
  elif config.WORST_FIT_BP:
    return worst_fit_bin_packing(task, cores)
  elif config.BEST_FIT_BP:
    return best_fit_bin_packing(task, cores)
  else:
    print('!!! ERROR: No bin-packing algorithm selected !!!')
    sys.exit()

# Find tasks with priority greater than Ti's (= tasks[i]) priority
def findHp (i, tasks, core_id):
  result = []
  task = tasks[i]
  for j in range(len(tasks)):
    if j == i:
      assert (tasks[j] == tasks[i]), 'Indexes did not match in findHp'
      continue
    other_task = tasks[j]
    if other_task['P'][core_id] < 0 or other_task['P'][core_id] > task['P'][core_id]:
      result.append(other_task)
  return result

# Find tasks with priority lower than Ti's (= tasks[i]) priority
def findLp (i, tasks, core_id):
  result = []
  task = tasks[i]
  for j in range(len(tasks)):
    if j == i:
      assert (tasks[j] == tasks[i]), 'Indexes did not match in findHp'
      continue
    other_task = tasks[j]
    if other_task['P'][core_id] < task['P'][core_id]:
      result.append(other_task)
  return result

# Vestal's algorithm (classic version)
def calcRi (task, hp):
  start_Ri = task['C(LO)'] + overhead_parameter.get_initial_overhead (config.PLATFORM)
  if task['HI']:
    start_Ri = task['C(HI)']
  Ri = start_Ri
  while True:
    newRi = start_Ri
    for hp_task in hp:
      hp_C = hp_task['C(LO)']
      # Only consider C(HI) interference if task i is HI-crit
      if task['HI']:
        hp_C = hp_task['C(HI)']
      newRi += math.ceil(Ri / hp_task['D']) * hp_C
    if newRi > task['D']:
      return None
    if newRi == Ri:
      return newRi
    Ri = newRi

# Vestal's algorithm (with monitor)
def calcRi_monitor (task, hp):
  start_Ri = task['C(LO)']
  if task['HI']:
    start_Ri = task['C(HI)']
  Ri = start_Ri
  while True:
    newRi = start_Ri + overhead_parameter.get_initial_overhead (config.PLATFORM)
    for hp_task in hp:
      hp_C = hp_task['C(LO)']
      # Only consider C(HI) interference if both task j and task i are HI-crit
      if task['HI'] and hp_task['HI']:
        hp_C = hp_task['C(HI)']
      newRi += math.ceil(Ri / hp_task['D']) * hp_C
    if newRi > task['D']:
      return None
    if newRi == Ri:
      return newRi
    Ri = newRi

# This modified version of Vestal's algorithm always considers HI-crit interference from HI-crit tasks
def calcRi_alwaysHICrit (task, hp, lp):
  start_Ri = task['C(LO)']
  if task['HI']:
    start_Ri = task['C(HI)']
  
  # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
  Ri = start_Ri + overhead_parameter.get_initial_overhead (config.PLATFORM)
  while True:
    newRi = start_Ri
    for hp_task in hp:
      hp_C = hp_task['C(LO)'] + overhead_parameter.get_refined_CLO (config.PLATFORM)
      # Only consider C(HI) interference if task i is HI-crit
      if hp_task['HI']:
        hp_C = hp_task['C(HI)'] + overhead_parameter.get_refined_CHI (config.PLATFORM)
      newRi += (math.ceil(Ri / hp_task['D']) * hp_C)
      # Add interference due to the "demanded" hp tasks clock overhead (see the previous link)
      newRi += (math.ceil(Ri / hp_task['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))

    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in lp:
      newRi += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")

    if newRi > task['D']:
      return None
    if newRi == Ri:
      return newRi
    Ri = newRi

def audsley_rta_no_migration (i, tasks, core_id):
  task = tasks[i]
  lp = findLp(i, tasks, core_id)
  hp = findHp(i, tasks, core_id)
  for hp_task in hp:
    assert (hp_task['P'][core_id] > task['P'][core_id] or hp_task['P'][core_id] < 0), 'Error: findHP returned task with wrong priority'
  Ri = None
  if (config.VESTAL_CLASSIC):
    Ri = calcRi(task, hp)
  elif (config.VESTAL_WITH_MONITOR):
    Ri = calcRi_monitor(task, hp)
  elif (config.ALWAYS_HI_CRIT):
    Ri = calcRi_alwaysHICrit(task, hp, lp)
  if Ri is None:
    return False
  assert (Ri <= task['D']), 'No migration algorithm produced a response time greater than the deadline'
  tasks[i]['Ri'] = Ri
  return True

# Find which task, in this core, has the longest deadline
# core_id -> id of core on which we are checking
# tasks -> core's tasks
# HI -> should we check HI-crit tasks or LO-crit tasks?
def find_lon_dead(core_id, tasks, HI):
  max_deadline = -1
  result = -1
  for i in range(len(tasks)):
    task = tasks[i]
    # Ensure that the task doesn't already have a priority for this core
    if task['P'][core_id] < 0 and task['HI'] == HI and task['D'] > max_deadline:
      max_deadline = task['D']
      result = i
  return result

def clear_priorities (tasks, core_id):
  for task in tasks:
    task['P'][core_id] = -1

# Implements Audsley's OPA
# core -> core object
# core_id -> core identifier
# audsley_rta -> RTA algorithm to use (no migration, Ri(LO), Ri(HI), etc.)
# side_effect -> Should the priorities assigned during this step be saved?
def audsley (core, core_id, audsley_rta, side_effect, is_last_task):
  # One priority for each task
  priority_levels = len(core['tasks'])
  # Clone tasks to avoid side effects
  verification_tasks = copy.deepcopy(core['tasks'])
  clear_priorities(verification_tasks, core_id)
  for p_lvl in range(priority_levels):
    # Find the HI-crit task with greatest deadline (and no priority for this core)
    lon_dead_HI_i = find_lon_dead(core_id, verification_tasks, True)
    if lon_dead_HI_i >= 0:
      lon_dead_HI = verification_tasks[lon_dead_HI_i]
      assert (lon_dead_HI['HI'] == True), 'Error extracting HI-crit task during audsley OPA'
      assert (lon_dead_HI['P'][core_id] < 0), 'Assigning priority to already prioritized HI-crit task'
      lon_dead_HI['P'][core_id] = p_lvl
      # Check if system schedulable with p_lvl priority assinged to to this task
      lon_dead_HI_result = audsley_rta(lon_dead_HI_i, verification_tasks, core_id)
      # If the result is True skip the next check and leave the priority assigned to the task
      if lon_dead_HI_result:
        continue
      # Otherwise reset the priority and check LO-crit tasks
      lon_dead_HI['P'][core_id] = -1
    # Find the LO-crit task with greatest deadline (and no priority for this core)
    lon_dead_LO_i = find_lon_dead(core_id, verification_tasks, False)
    if lon_dead_LO_i >= 0:
      lon_dead_LO = verification_tasks[lon_dead_LO_i]
      assert (lon_dead_LO['HI'] == False), 'Error extracting LO-crit task during audsley OPA'
      assert (lon_dead_LO['P'][core_id] < 0), 'Assigning priority to already prioritized LO-crit task'
      lon_dead_LO['P'][core_id] = p_lvl
      lon_dead_LO_result = audsley_rta(lon_dead_LO_i, verification_tasks, core_id)
      if lon_dead_LO_result:
        continue
      lon_dead_LO['P'][core_id] = -1
    return False
  
  # In some cases we want to remember the priorities assigned at this point
  if side_effect:
    core['tasks'] = verification_tasks
  else:
    config.last_time_on_core_i[core_id] = verification_tasks

  for task in verification_tasks:
    assert(task['P'][core_id] >= 0), 'Audsley OPA did not assign priority to some task'

  return True

def verify_RTA_migration (cores, hi_crit_core_id, migration_core_id):
  is_RTA_needed = False
  for task in cores[hi_crit_core_id]['tasks']:
    if task['migrating']:
      is_RTA_needed = True
      break
  
  if is_RTA_needed == False:
    # since there's no tasks migrating, we can conclude that no tasks of hi_crit_core_id
    # migrates to migration_core_id => migration_core_id is still (trivially) feasible
    return True

  # Always clone cores to avoid side effects
  verification_cores = copy.deepcopy(cores)

  # Get clone of the core to check for schedulability
  verification_core = verification_cores[migration_core_id]

  # Simulate assigning the hi_crit_core_id's migrating tasks to migration_core_id
  for task in verification_cores[hi_crit_core_id]['tasks']:
    if task['migrating']:
      verification_cores[migration_core_id]['tasks'].append(task)
  
  # Let's check if migration_core_id is still feasibile with the addition of migrating tasks.
  if not audsley(verification_cores[migration_core_id], migration_core_id, audsleyRiLO_1, True, False):
    return False

  for task in verification_cores[migration_core_id]['tasks']:
    assert (task['P'][migration_core_id] >= 0), 'Side effects did not work for Ri(LO)_1'
  config.last_time_on_core_i_with_additional_migrating_task[migration_core_id] = verification_cores[migration_core_id]['tasks']

  # Verify 2nd crit core
  # RTA for new HI-crit cores after the SAFE boundary number is reached
  # Calculate Ri(LO) and Ri(LO'), necessary for Ri(HI)
  audsley(verification_cores[migration_core_id], migration_core_id, audsley_rta_steady, True, False)
  for task in verification_cores[migration_core_id]['tasks']:
    assert (task['P'][migration_core_id] >= 0), "Side effect did not work"
  
  if not verifyRiHI_1(verification_cores[migration_core_id], migration_core_id):
    return False
  # config.where_last_mod_mig = "RTA mig"
  # config.last_time_on_core_i_with_additional_migrating_task[migration_core_id] = verification_cores[migration_core_id]['tasks']
  return True

def TSP_2_schema_step (partitions, slices_duration):
  #print(partitions, "\n")
  #print(slices_duration, "\n", "--")
  for partition in partitions:
    slice_duration = slices_duration[partition]
    other_slice_duration = (slices_duration['LOW'] if partition == 'HIGH' else slices_duration['HIGH'])
    partitions[partition]['tasks'] = sorted (partitions[partition]['tasks'], key = lambda t: t['Ri'])

    for task in partitions[partition]['tasks']:
      deactived_time = math.floor(task['Ri'] / slice_duration) * other_slice_duration
      Ri_TSP = task['Ri'] + deactived_time + other_slice_duration
      if Ri_TSP > task['D']:
        return False
  
  return True

def verify_schedulability_TSP_schema_2 ():
  # print("Verify TSP2")
  partitions = ['HIGH', 'LOW']
  cores = ['c1', 'c2']
  system = {}
  deadlines = {cores[0]: [], cores[1]: []}
  slices_duration = {
    cores[0]: {partitions[0]: 0.0, partitions[1]: 0.0},
    cores[1]: {partitions[0]: 0.0, partitions[1]: 0.0}
  }

  for core in cores:
    system[core] = {}
    for p in partitions:
      system[core][p] = {'tasks': [], 'totalutil': 0.0}

  # for each core, split the taskset into the two partitions
  for core in config.last_time_on_core_i:
    for task in config.last_time_on_core_i[core]:
      if task['HI']:
        # HI-crit partition
        system[core]['HIGH']['tasks'].append(task.copy())
        system[core]['HIGH']['totalutil'] += task['U']
      else:
        # LO-crit partition
        system[core]['LOW']['tasks'].append(task.copy())
        system[core]['LOW']['totalutil'] += task['U']

      deadlines[core].append(task['D'])

  for core in system:
    # weighted round-robin
    LO_HI_ratio = system[core]['LOW']['totalutil'] / system[core]['HIGH']['totalutil']
    biggest_slice = math.floor(min(deadlines[core])) #+ overhead_parameter.get_partition_context_switch (config.TSP_PLATFORM) + overhead_parameter.get_hypervisor_metric (config.TSP_PLATFORM, "Clock_Management")
    if LO_HI_ratio > 1:
      # LO-crit partition is the loadest one
      slices_duration[core]['LOW'] = biggest_slice
      slices_duration[core]['HIGH'] = math.floor(biggest_slice / LO_HI_ratio)
    else:
      # HI-crit partition is the loadest one
      slices_duration[core]['HIGH'] = biggest_slice
      slices_duration[core]['LOW'] = math.floor(biggest_slice * LO_HI_ratio)

    factor = 2
    # print ("----")
    while True:
      # print(slices_duration[core])
      is_schedulable = TSP_2_schema_step (partitions=system[core], slices_duration=slices_duration[core])
      if is_schedulable:
        break
      
      for partition in slices_duration[core]:
        slices_duration[core][partition] = math.floor(slices_duration[core][partition] / factor)
        if slices_duration[core][partition] <= 0:
          return False

  for core in system:
    for partition in system[core]:
      config.slices_duration[core][partition] = slices_duration[core][partition]
  return True

# schemes are described in section 2.2.3 of this document:
# https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/8
# Avalaible schemes:
#   - 1 -> 1 core, 1 partition
#   - 2 -> a partition for each criticality level
def verify_schedulability_TSP (schema):
  # schema 1 makes "irrelevant" hierarchical scheduling
  if schema == 1:
    return True
  if schema == 2:
    return verify_schedulability_TSP_schema_2 ()

# is_last_task: True iff task is the last one that we are checking. If this task is schedulable,
# then so is the whole systems.
def verify_no_migration_task (task, cores, is_last_task, is_no_migration_algo):
  # Cleanup "considered" flag on cores to start fresh for the new task
  reset_considered(cores)
  assigned = False
  count = 0
  next_core = -1
  considered_cores = []
  while not assigned and count < 2:
    count += 1
    next_core = get_next_core(task, cores)
    assert (next_core not in considered_cores), 'Picked the same core 2 times'
    considered_cores.append(next_core)
    if next_core is None:
      return False
    cores[next_core]['considered'] = True
    # Always clone cores to avoid side effects
    verification_cores = copy.deepcopy(cores)
    verification_core = copy.deepcopy(cores[next_core])
    verification_core['tasks'].append(task)
    # Check core schedulability with Audsley's OPA

    if next_core == 'c1':
      other_core = 'c2'
    elif next_core == 'c2':
      other_core = 'c1'

    backup_tasks = copy.deepcopy(cores[next_core]['tasks'])
    backup_U = copy.deepcopy(cores[next_core]['utilization'])

    if audsley(verification_core, next_core, audsley_rta_no_migration, False, is_last_task):
      cores[next_core]['tasks'] = verification_core['tasks']
      for task in cores[next_core]['tasks']:
        assert (task['P'][next_core] < 0), 'No migration algorithm assigned side effect priority'
      cores[next_core]['utilization'] += task['U']

      if not (is_no_migration_algo) and not (verify_RTA_migration(cores, other_core, next_core)):
        cores[next_core]['tasks'] = copy.deepcopy(backup_tasks)
        cores[next_core]['utilization'] = copy.deepcopy(backup_U)
        return False

      assigned = True

  return assigned

# Calculate Ri(LO) (cfr. Equation 7 in Xu, Burns 2019)
def calcRiLO (task, hp, lp):
  RiLO = task['C(LO)'] + overhead_parameter.get_initial_overhead (config.PLATFORM)
  while True:
    newRiLO = task['C(LO)']
    task['Interference_LO'] = 0
    for hp_task in hp:
      newRiLO += math.ceil(RiLO / hp_task['D']) * (hp_task['C(LO)'] + overhead_parameter.get_refined_CLO (config.PLATFORM))
      task['Interference_LO'] += math.ceil(RiLO / hp_task['D']) * hp_task['C(LO)']
      # Add interference due to the "demanded" hp tasks clock overhead
      # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
      newRiLO += (math.ceil(RiLO / hp_task['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))

    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in lp:
      newRiLO += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")

    if newRiLO > task['D']:
      return None
    if newRiLO == RiLO:
      if 'Ri(LO)' not in task:
        # Update Jitter and Deadline for next steps
        task['J'] = task['J'] + (RiLO - task['C(LO)'])
        task['D1'] = task['D'] - (RiLO - task['C(LO)'])
        task['Ri(LO)'] = RiLO
      return newRiLO
    RiLO = newRiLO

def findCHp (task, tasks, core_id):
  result = []
  for other_task in tasks:
    if not other_task['migrating'] and (other_task['P'][core_id] > task['P'][core_id]):
      result.append(other_task)
  return result

def findCHp_lp (task, tasks, core_id):
  result = []
  for other_task in tasks:
    if not other_task['migrating'] and (other_task['P'][core_id] < task['P'][core_id]):
      result.append(other_task)
  return result

def findCHpHI (task, tasks, core_id):
  result = []
  for other_task in tasks:
    assert (other_task['P'][core_id] >= 0), 'No priorities assigned for this core'
    if other_task['HI'] and (other_task['P'][core_id] > task['P'][core_id]):
      result.append(other_task)
  return result

def findCHpLO (task, tasks, core_id):
  result = []
  for other_task in tasks:
    assert (other_task['P'][core_id] >= 0), 'No priorities assigned for this core'
    if not other_task['HI'] and (other_task['P'][core_id] > task['P'][core_id]):
      result.append(other_task)
  return result

def findCHpHI_lp (task, tasks, core_id):
  result = []
  for other_task in tasks:
    assert (other_task['P'][core_id] >= 0), 'No priorities assigned for this core'
    if other_task['HI'] and (other_task['P'][core_id] < task['P'][core_id]):
      result.append(other_task)
  return result

def findCHpLO_lp (task, tasks, core_id):
  result = []
  for other_task in tasks:
    assert (other_task['P'][core_id] >= 0), 'No priorities assigned for this core'
    if not other_task['HI'] and (other_task['P'][core_id] < task['P'][core_id]):
      result.append(other_task)
  return result

def findCHpMIG (task, tasks, core_id):
  result = []
  for other_task in tasks:
    if other_task['migrating'] and (other_task['P'][core_id] > task['P'][core_id]):
      result.append(other_task)
  return result

def findCHpMIG_lp (task, tasks, core_id):
  result = []
  for other_task in tasks:
    if other_task['migrating'] and (other_task['P'][core_id] < task['P'][core_id]):
      result.append(other_task)
  return result

def riMIXStep (task, chp, chpMIG, chp_lp, chpMIG_lp):
  start_val = task['C(LO)']
  if task['HI']:
    start_val = task['C(HI)']
  RiMIX = start_val + overhead_parameter.get_initial_overhead (config.PLATFORM)
  while True:
    newRiMIX = start_val
    for chp_task in chp:
      chp_val = chp_task['C(LO)'] + overhead_parameter.get_refined_CLO (config.PLATFORM)
      if chp_task['HI']:
        chp_val = chp_task['C(HI)'] + overhead_parameter.get_refined_CHI (config.PLATFORM)
      newRiMIX += math.ceil(RiMIX / chp_task['D']) * chp_val
      # Add interference due to the "demanded" hp tasks clock overhead
      # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
      newRiMIX += (math.ceil(RiMIX / chp_task['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))

    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in chp_lp:
      newRiMIX += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")

    for chp_mig in chpMIG:
      newRiMIX += math.ceil(task['Ri(LO)'] / chp_mig['D']) * (chp_mig['C(LO)'] + overhead_parameter.get_refined_CLO (config.PLATFORM))
      # Add interference due to the "demanded" hp tasks clock overhead
      # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
      newRiMIX += (math.ceil(RiMIX / chp_mig['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))

    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in chpMIG_lp:
      newRiMIX += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")
    
    if newRiMIX > task['D']:
      return None
    if newRiMIX == RiMIX:
      task['Ri(MIX)'] = RiMIX
      return RiMIX
    RiMIX = newRiMIX

def audsleyRiMIX (i, tasks, core_id):
  task = tasks[i]
  if not task['migrating']:
    chp = findCHp(task, tasks, core_id)
    chpMIG = findCHpMIG(task, tasks, core_id)
    chp_lp = findCHp_lp(task, tasks, core_id)
    chpMIG_lp = findCHpMIG_lp(task, tasks, core_id)

    if riMIXStep(task, chp, chpMIG, chp_lp, chpMIG_lp) is None:
      return False
  return True

# Calculate Ri(MIX) (cfr. Equation 9 in Xu, Burns 2019 and Equation 11 in Xu, Burns 2015)
def verify_RiMIX (core, core_id):
  for i in range(len(core['tasks'])):
    assert (core['tasks'][i]['P'][core_id] >= 0), 'Attempting to run RiMIX on task with no priority for current core'
    if not audsleyRiMIX(i, core['tasks'], core_id):
      return False
  return True

def riLO_1Step (task, chp, lp, core_id):
  RiLO_1 = task['C(LO)'] + overhead_parameter.get_initial_overhead (config.PLATFORM)
  task_deadline = task['D']
  if (task['migrating'] and core_id in task['migration_route']):
    assert ('Ri(LO)' in task), 'Migrating task with no response time in steady mode found'
    task_deadline = task['D1']
  while True:
    newRiLO_1 = task['C(LO)']
    for chp_task in chp:
      chp_jitter = 0
      if (chp_task['migrating'] and core_id in chp_task['migration_route']):
        chp_jitter = chp_task['J']
      newRiLO_1 += math.ceil((RiLO_1 + chp_jitter) / chp_task['D']) * (chp_task['C(LO)']  + overhead_parameter.get_refined_CLO (config.PLATFORM))
      # Add interference due to the "demanded" hp tasks clock overhead
      # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
      newRiLO_1 += (math.ceil(RiLO_1 / chp_task['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))

    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in lp:
      newRiLO_1 += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")

    if newRiLO_1 > task_deadline:
      return None
    if newRiLO_1 == RiLO_1:
      # if 'Ri(LO)' in task:
      #   task['J2'] = task['J'] + (RiLO_1 - task['C(LO)'])
      #   task['D2'] = task['D1'] - (RiLO_1 - task['C(LO)'])
      task['Ri(LO)_1'] = RiLO_1
      return RiLO_1
    RiLO_1 = newRiLO_1

# Calculate Ri(LO)' with Audsley's OPA (cfr. Equation 9 in Xu, Burns 2019 and in Xu, Burns 2015)
def audsleyRiLO_1 (i, tasks, core_id):
  task = tasks[i]
  chp = findHp(i, tasks, core_id)
  lp = findLp(i, tasks, core_id)
  if riLO_1Step(task, chp, lp, core_id) is None:
    return False
  return True

def riHI_1Step (task, chpHI, chpLO, chpHI_lp, chpLO_lp, core_id):
  RiHI_1 = task['C(HI)'] + overhead_parameter.get_initial_overhead (config.PLATFORM)
  task_deadline = task['D']
  if (task['migrating'] and core_id == task['migration_route'][0]):
    task_deadline = task['D1']
  # elif (task['migrating'] and core_id == task['migration_route'][1]):
  #  task_deadline = task['D2']
  task_RiLO = -1
  if 'Ri(LO)_1' in task:
    task_RiLO = task['Ri(LO)_1']
  else:
    task_RiLO = task['Ri(LO)']
  assert (task_RiLO >= 0), 'No Ri(LO) assigned to task in Ri(HI)'
  # assert (task_RiLO == task['Ri(LO)_1']), 'Ri(HI)** has not Ri(LO)_1'
  while True:
    newRiHI_1 = task['C(HI)']
    for chp_task in chpHI:
      newRiHI_1 += math.ceil(RiHI_1 / chp_task['D']) * (chp_task['C(HI)'] + overhead_parameter.get_refined_CHI (config.PLATFORM))
      # Add interference due to the "demanded" hp tasks clock overhead
      # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
      newRiHI_1 += (math.ceil(RiHI_1 / chp_task['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))
    
    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in chpHI_lp:
      newRiHI_1 += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")

    for chp_task in chpLO:
      chp_jitter = 0
      # if (chp_task['migrating'] and core_id == chp_task['migration_route'][0]):
      #  chp_jitter = chp_task['J']
      # elif (chp_task['migrating'] and core_id == chp_task['migration_route'][1]):
      #  chp_jitter = chp_task['J2']
      newRiHI_1 += math.ceil((task_RiLO + chp_jitter) / chp_task['D']) * (chp_task['C(LO)'] + overhead_parameter.get_refined_CLO (config.PLATFORM))
      # Add interference due to the "demanded" hp tasks clock overhead
      # see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
      newRiHI_1 += (math.ceil(task_RiLO / chp_task['D']) * overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler"))

    # Add interference due to the "demanded" lp tasks clock overhead (see the previous link)
    for lp_task in chpLO_lp:
      newRiHI_1 += overhead_parameter.get_runtime_metric (config.PLATFORM, "clock handler")

    if newRiHI_1 > task_deadline:
      return None
    if newRiHI_1 == RiHI_1:
      task['Ri(HI)_2'] = RiHI_1
      return RiHI_1
    RiHI_1 = newRiHI_1

def audsleyRiHI_1 (i, tasks, core_id):
  task = tasks[i]
  if task['HI']:
    chpHI = findCHpHI(task, tasks, core_id)
    chpLO = findCHpLO(task, tasks, core_id)
    chpHI_lp = findCHpHI(task, tasks, core_id)
    chpLO_lp = findCHpLO(task, tasks, core_id)
    if riHI_1Step(task, chpHI, chpLO, chpHI_lp, chpLO_lp, core_id) is None:
      return False
  return True

# Calculate Ri(HI)** (cfr. Equation 13 in Xu, Burns 2015)
def verifyRiHI_1 (core, core_id):
  for i in range(len(core['tasks'])):
    if not audsleyRiHI_1(i, core['tasks'], core_id):
      return False
  return True

# verify criticality change progress in dual-core version. 
# Watchout: equations in dual-core work (https://dl.acm.org/doi/10.1145/2834848.2834865) follows different notations then the quad-core one.
# For instance, Ri(MIX) in Eq. 9 in quad-core work is R(HI)* in Eq. 11 in dual-core work.
# is_last_task: True iff task is the last one that we are checking. If this task is schedulable,
# then so is the whole systems.
def verify_mode_changes (cores, is_last_task):
  tasks_aux = []
  for mode_change in config.CORES_MODE_CHANGES:
    crit_count = 0
    verification_cores = copy.deepcopy(cores)
    migration_cores = []
    for crit_core in mode_change:
      # Calculate Ri(LO) (necessary for Ri(MIX))
      audsley(verification_cores[crit_core], crit_core, audsley_rta_steady, True, is_last_task)
      config.last_time_on_core_i[crit_core] = verification_cores[crit_core]['tasks']
      for task in verification_cores[crit_core]['tasks']:
        assert(task['P'][crit_core] >= 0), 'Crit core tasks do not have steady priorities'
        assert('Ri(LO)' in task), 'No Ri(LO) for tasks in crit core'
      current_migration_cores = []
      new_crit_core_tasks = []
      for task in verification_cores[crit_core]['tasks']:
        if not task['migrating']:
          new_crit_core_tasks.append(task)
        else:
          # Always attempt to migrate to the first migration core
          migration_core = task['migration_route'][0]
          # If it is already in HI-crit mode, migrate to the second
          # if crit_count > 0 and (migration_core == mode_change[0] or migration_core == crit_core):
          #  migration_core = task['migration_route'][1]
          assert (verification_cores[migration_core]['crit'] == False), 'Attempting to migrate to a HI-crit core'
          verification_cores[migration_core]['tasks'].append(task)
          if migration_core not in current_migration_cores:
            current_migration_cores.append(migration_core)
          if migration_core not in migration_cores:
            migration_cores.append(migration_core)
      # RTA for new HI-crit core
      # This uses the priorities assigned during the steady mode, no Audsley here
      if not verify_RiMIX(verification_cores[crit_core], crit_core):
        return False
      # config.last_time_on_core_i[crit_core] = verification_cores[crit_core]['tasks']
      # Remove migrated tasks from HI-crit core
      # This is done to test future interferences
      verification_cores[crit_core]['tasks'] = new_crit_core_tasks
      for task in verification_cores[crit_core]['tasks']:
        assert(task['migrating'] == False), 'Migrating task remained in HI-crit core'
      # RTA for cores which receive migrated tasks
      for m_c in current_migration_cores:
        if not audsley(verification_cores[m_c], m_c, audsleyRiLO_1, True, is_last_task):
          return False

        m_c_aux = m_c
        tasks_aux = verification_cores[m_c]['tasks']
        config.where_last_mod_mig = "mode change"
        config.last_time_on_core_i_with_additional_migrating_task[m_c] = verification_cores[m_c]['tasks']
        
        for task in verification_cores[m_c]['tasks']:
          assert (task['P'][m_c] >= 0), 'Side effects did not work for Ri(LO)_1'
          
      crit_count += 1
    for core_id in verification_cores:
      # Verify 2nd crit core
      if core_id not in mode_change:
        # RTA for new HI-crit cores after the SAFE boundary number is reached
        # Calculate Ri(LO) and Ri(LO'), necessary for Ri(HI)
        if core_id not in migration_cores:
          audsley(verification_cores[core_id], core_id, audsley_rta_steady, True, is_last_task)
          for task in verification_cores[core_id]['tasks']:
            assert (task['P'][core_id] >= 0), "Side effect did not work"

        #audsley(verification_cores[core_id], core_id, audsleyRiLO_1, True)
        if not verifyRiHI_1(verification_cores[core_id], core_id):
          return False
        # if tasks_aux:
          # config.last_time_on_core_i_with_additional_migrating_task[m_c_aux] = tasks_aux
        
        # config.last_time_on_core_i_with_additional_migrating_task[core_id] = verification_cores[core_id]['tasks']
        # if is_last_task:
          # print("Ok RTA for new HI-crit cores after the SAFE boundary number is reached")
          #utils. print_taskset(verification_cores['c1']['tasks'], verification_cores['c2']['tasks'])

  return True

# This function applies Audsley's OPA to the steady mode
def audsley_rta_steady (i, tasks, core_id):
  task = tasks[i]
  # Get LO-crit and HI-crit higher priority tasks
  hp = findHp(i, tasks, core_id)
  lp = findLp(i, tasks, core_id)
  RiLO = calcRiLO(task, hp, lp)
  if RiLO is None:
    return False
  assert (RiLO <= task['D']), 'RiLO returned response time greater than deadline'
  assert (task['D1'] <= task['D']), 'Deadline D1 should be <= D'
  return True

# This function returns the LO-crit tasks of a core
# sorted by priority
def get_LO_crit_tasks (tasks, core_id):
  result = []
  for i in range(len(tasks)):
    task = tasks[i]
    if not task['HI'] and not task['migrating']:
      result.append([i, task])
  if core_id == 'c1':
    result.sort(key=functools.cmp_to_key(utils.sort_tasks_priority_c1))
  elif core_id == 'c2':
    result.sort(key=functools.cmp_to_key(utils.sort_tasks_priority_c2))

  return [r[0] for r in result]

def backup_priorities (tasks):
  result = []
  for task in tasks:
    result.append(task['P'])
  return result

def assign_backup_priorities(core, bkp_priorities):
  for i in range(len(core['tasks'])):
    core['tasks'][i]['P'] = bkp_priorities[i]

# is_last_task: True iff task is the last one that we are checking. If this task is schedulable,
# then so is the whole systems.
def verify_migration_task (task, cores, is_last_task, fetched_approach):
  # Cleanup "considered" flag on cores to start fresh for the new task
  # if is_last_task:
    # print ("last task is mig")
  reset_considered(cores)
  assigned = False
  count = 0
  considered_cores = []
  while not assigned and count < 2:
    count += 1
    next_core = get_next_core(task, cores)
    assert (next_core not in considered_cores), 'Picked the same core 2 times'
    considered_cores.append(next_core)
    if next_core is None:
      return False
    cores[next_core]['considered'] = True
    # Always clone cores and tasks to avoid side effects
    verification_task = copy.deepcopy(task)
    verification_cores = copy.deepcopy(cores)
    # Get clone of the core to check for schedulability
    verification_core = verification_cores[next_core]
    # Simulate assigning the task to the core
    verification_core['tasks'].append(verification_task)
    # Check steady mode
    if audsley(verification_core, next_core, audsley_rta_steady, True, is_last_task):
      # config.last_time_on_core_i[next_core] = verification_core['tasks']
      
      for task in verification_core['tasks']:
        assert(task['P'][next_core] >= 0), 'Side effects did not work for steady mode verification'

      assigned_migrating = False
      # priorities_backup = backup_priorities(verification_core['tasks'])
      verification_cores_mode = copy.deepcopy(verification_cores)
      
      if fetched_approach:
        for T in verification_cores_mode[next_core]['tasks']:
          if T['ID'] == task['ID']:
            verification_task_mode = T
            break
        assert (verification_task_mode['ID'] == task['ID']), 'Fetched approach fails.'
        assert (verification_task_mode['HI'] == False), 'Only LO-crit tasks should be eligible for migration'
        assert (verification_task_mode['migrating'] == False), 'Already migrating LO-crit task selected for migration'
        verification_task_mode['migrating'] = True
        # Try to assign the task to each migration group until a schedulable configuration
        # is found or all routes are tested
        for migration_group in cores[next_core]['migration']:
          verification_task_mode['migration_route'] = migration_group
          # Every migrating task must have new priorities in the landing core
          for core in migration_group:
            verification_task_mode['P'][core] = -1
          # Verify mode changes
          if verify_mode_changes(verification_cores_mode, is_last_task):
            assigned_migrating = True
            assigned = True
            cores[next_core]['tasks'] = verification_cores_mode[next_core]['tasks']
            # config.last_time_on_core_i_with_additional_migrating_task[next_core] = verification_cores_mode[next_core]['tasks']
            cores[next_core]['utilization'] += task['U']
            for t in config.last_time_on_core_i_with_additional_migrating_task[next_core]:
              if t['migrating']:
                for t2 in config.last_time_on_core_i[next_core]:
                  if t['ID'] == t2['ID']:
                    t2['migrating'] = True
                    break
                break
            break
      else:
        # Tasks verified for steady mode, with priority and Ri(LO), C(LO), etc.
        # Get the LO-crit (non-migrating) tasks, sorted by priority
        # Note: this is done in descending priority order (cfr. Semi2 model)
        LO_crit_tasks = get_LO_crit_tasks(verification_core['tasks'], next_core)
        for LO_crit_task_i in LO_crit_tasks:
          # assign_backup_priorities(verification_cores_mode[next_core], priorities_backup) # TODO: non necessario perche' gia' si fa il clone?
          verification_task_mode = verification_cores_mode[next_core]['tasks'][LO_crit_task_i]
          assert (verification_task_mode['HI'] == False), 'Only LO-crit tasks should be eligible for migration'
          assert (verification_task_mode['migrating'] == False), 'Already migrating LO-crit task selected for migration'
          verification_task_mode['migrating'] = True
          # Try to assign the task to each migration group until a schedulable configuration
          # is found or all routes are tested
          for migration_group in cores[next_core]['migration']:
            verification_task_mode['migration_route'] = migration_group
            # Every migrating task must have new priorities in the landing core
            for core in migration_group:
              verification_task_mode['P'][core] = -1
            # Verify mode changes
            if verify_mode_changes(verification_cores_mode, is_last_task):
              assigned_migrating = True
              assigned = True
              cores[next_core]['tasks'] = verification_cores_mode[next_core]['tasks']
              # config.last_time_on_core_i_with_additional_migrating_task[next_core] = verification_cores_mode[next_core]['tasks']
              cores[next_core]['utilization'] += task['U']
              for t in config.last_time_on_core_i[next_core]:
                if t['ID'] == verification_task_mode['ID']:
                  t['migrating'] = True
                  break
              break
          if assigned_migrating:
            break

      if assigned_migrating:
        break
  if not assigned:
    return False

  return True

def reset_all_priorities (cores):
  for c in cores:
    core = cores[c]
    for task in core['tasks']:
      task['P'] = {'c1': -1, 'c2': -1}

# Point of entry for all the tests
# 1. No migration model: Vestal's algorithm
# 2. Model 1: 1 migration route for every core

def verify_no_migration (taskset, is_no_migration_algo):
  cores = copy.deepcopy(config.CORES_NO_MIGRATION)
  is_last_task = False
  i = 1

  for task in taskset:
    if i >= len(taskset):
      is_last_task = True
    reset_all_priorities(cores)
    if not verify_no_migration_task(task, cores, is_last_task, is_no_migration_algo):
      return False
    i = i + 1
      
  scheduled_tasks = 0
  for c in cores:
    scheduled_tasks += len(cores[c]['tasks'])
  assert (scheduled_tasks == len(taskset)), 'No migration: Scheduled a number of task different than the taskset size'
  return True

def verify_model_1 (taskset, fetched_approach):
  i = 1
  config.where_last_mod_mig = ""
  config.last_time_on_core_i = {'c1': [], 'c2': []}
  config.last_time_on_core_i_with_additional_migrating_task = {'c1': [], 'c2': []}
  is_last_task = False
  cores = copy.deepcopy(config.CORES_MODEL_1)
  # system = copy.deepcopy(config.SYSTEM_MODEL)

  for task in taskset:
    if i >= len(taskset):
      is_last_task = True
    reset_all_priorities(cores)
    # Attempt assigning with no migration
    if not verify_no_migration_task(task, cores, is_last_task, False):
      # Otherwise attempt migration
      if task['HI'] or not verify_migration_task(task, cores, is_last_task, fetched_approach):
        return False
    i = i + 1

  scheduled_tasks = 0
  for c in cores:
    scheduled_tasks += len(cores[c]['tasks'])
  assert (scheduled_tasks == len(taskset)), 'Model 1: Scheduled a number of task different than the taskset size'
  return True
