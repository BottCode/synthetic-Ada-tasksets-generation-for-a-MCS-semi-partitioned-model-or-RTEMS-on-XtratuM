import copy
import config

# Define sorting functions for each core to be given to the standard list sorting function
def sort_tasks_priority_c1 (t1, t2):
  if t1[1]['P']['c1'] >= t2[1]['P']['c1']:
    return -1
  else:
    return 1

def sort_tasks_priority_c2 (t1, t2):
  if t1[1]['P']['c2'] >= t2[1]['P']['c2']:
    return -1
  else:
    return 1

def print_taskset (core_1, core_2):
  if len (core_1) > 0:
    print ("Core 1")
    for task in core_1:
      print (task)

  if len (core_2) > 0:
    print ("Core 2")
    for task in core_2:
      print (task)

def check_size_taskset_with_mig (total):
  assert(len(config.last_time_on_core_i['c1']) + len(config.last_time_on_core_i['c2']) == total), "Wrong number of scheduled tasks"
  cores = ['c1', 'c2']
  # is there at least one migrating task on c_i?
  mig_on_c_i = {'c1': False, 'c2': False}

  comparing_steady_mode = copy.deepcopy(config.last_time_on_core_i)
  comparing_migration_mode = copy.deepcopy(config.last_time_on_core_i_with_additional_migrating_task)

  migrating_tasks = []

  other_core = 'c2'

  for core in cores:
    if core == 'c1':
      other_core = 'c2'
    else:
      other_core = 'c1'
    for task in config.last_time_on_core_i[core]:
      if task['migrating']:
        mig_on_c_i[core] = True
        migrating_tasks.append(task)
        comparing_migration_mode[other_core].append(task)

  if mig_on_c_i['c1']:
    assert(len(config.last_time_on_core_i_with_additional_migrating_task['c2']) > 0), 'c2 should have migrating tasks'
    for task_mig in migrating_tasks:
      find = False
      for task in config.last_time_on_core_i_with_additional_migrating_task['c2']:
        if task_mig['ID'] == task['ID']:
          find = True
          break
      if not find:
        assert(find)
        print(task_mig['ID'], "not found in c2")
        break

    for task in config.last_time_on_core_i['c2']:
      find = False
      for t2 in config.last_time_on_core_i_with_additional_migrating_task['c2']:
        if task['ID'] == t2['ID']:
          find = True
          break
      if not find:
        assert(find)
        print(task['ID'], "is missing in c2")
  else:
    #assert(len(config.last_time_on_core_i_with_additional_migrating_task['c2']) <= 0), 'c2 should NOT have migrating tasks'
    if not (len(config.last_time_on_core_i_with_additional_migrating_task['c2']) <= 0):
      print('c2 should NOT have migrating tasks')
      # @TODO: you are cheating...
      config.last_time_on_core_i_with_additional_migrating_task['c2'] = []

  if mig_on_c_i['c2']:
    assert(len(config.last_time_on_core_i_with_additional_migrating_task['c1']) > 0), 'c1 should have migrating tasks'
    for task_mig in migrating_tasks:
      find = False
      for task in config.last_time_on_core_i_with_additional_migrating_task['c1']:
        if task_mig['ID'] == task['ID']:
          find = True
          break
      if not find:
        assert(find)
        print(task_mig['ID'], "not found in c1")
        break

    for task in config.last_time_on_core_i['c1']:
      find = False
      for t2 in config.last_time_on_core_i_with_additional_migrating_task['c1']:
        if task['ID'] == t2['ID']:
          find = True
          break
      if not find:
        print(task['ID'], "is missing in c2")
        assert(find)
        break
  else:
    #assert(len(config.last_time_on_core_i_with_additional_migrating_task['c1']) <= 0), 'c1 should NOT have migrating tasks'
    if not (len(config.last_time_on_core_i_with_additional_migrating_task['c1']) <= 0):
      print('c1 should NOT have migrating tasks')
      # @TODO: you are cheating...
      config.last_time_on_core_i_with_additional_migrating_task['c1'] = []



  




