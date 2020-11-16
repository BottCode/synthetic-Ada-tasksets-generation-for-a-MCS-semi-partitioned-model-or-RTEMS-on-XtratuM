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

def check_size_taskset_with_mig (core_1, core_2, total):
  if len (core_1) + len (core_2) > 0:
    mig_on_c1  = False
    mig_on_c2 = False
    mig_c1 = 0
    mig_c2 = 0

    for task in core_1:
      if task['migrating']:
        mig_c1 += 1
        mig_on_c1 = True

    for task in core_2:
      if task['migrating']:
        mig_c2 += 1
        mig_on_c2 = True

    if mig_on_c1 and mig_on_c2:
      assert (len(core_1) + len(core_2) + mig_on_c1 + mig_on_c2 == total + mig_on_c1 + mig_on_c2), "Double priority migrating is INCORRECT"
    else:
      assert (len(core_1) + len(core_2) == total), print_taskset(core_1, core_2)

  




