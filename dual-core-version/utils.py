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
  cores = ['c1', 'c2']
  # is there at least one migrating task on c_i?
  mig_on_c_i = {'c1': False, 'c2': False}

  comparing_steady_mode = copy.deepcopy(config.last_time_on_core_i)
  comparing_migration_mode = copy.deepcopy(config.last_time_on_core_i_with_additional_migrating_task)

  other_core = 'c2'

  for core in cores:
    if core == 'c1':
      other_core = 'c2'
    else:
      other_core = 'c1'
    for task in config.last_time_on_core_i[core]:
      if task['migrating']:
        mig_on_c_i[core] = True
        comparing_migration_mode[other_core].append(task)
  
  for core in cores:
    if core == 'c1':
      other_core = 'c2'
    else:
      other_core = 'c1'
      
    for task in config.last_time_on_core_i_with_additional_migrating_task[core]:
      for t in comparing_migration_mode[core]:
        if t['ID'] == task['ID']:
          comparing_migration_mode[core].remove(t)
          break

  # assert (len(comparing_migration_mode['c1']) + len(comparing_migration_mode['c2']) == 0), print(comparing_migration_mode['c1'], comparing_migration_mode['c2'])
  if len(comparing_migration_mode['c1']) + len(comparing_migration_mode['c2']) != 0:
    print("--  WHATCHOUT --")
    print_taskset(comparing_migration_mode['c1'], comparing_migration_mode['c2'])
    print ("WRONG")


  




