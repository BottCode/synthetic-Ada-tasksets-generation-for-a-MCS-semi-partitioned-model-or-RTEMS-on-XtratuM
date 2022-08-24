import numpy
import math
import random
import functools
import config
import perale_taskset_generator
import sys
from drs import drs

# Default values taken from "Techniques For The Synthesis Of Multiprocessor Tasksets" by Emberson, et. al
# cfr. https://www.researchgate.net/publication/241677949_Techniques_For_The_Synthesis_Of_Multiprocessor_Tasksets
def log_uniform (n, Tmin = 50, Tmax = 250, Tg = 10):
  R = numpy.random.uniform(math.log(Tmin), math.log(Tmax + Tg), n)
  T = []
  for ri in R:
    T.append(math.floor(math.exp(ri) / Tg) * Tg)
  return T

def UUnifast_discard_step (n, maxU):
  sumU = maxU
  U = []
  for i in range (1, n):
    nextSumU = sumU * (numpy.random.uniform() ** (1 / (n - i)))
    U.append(sumU - nextSumU)
    sumU = nextSumU
  U.append(sumU)
  # "Discard" step, if one of the utilizations is > 1 drop all the results
  for i in range(0, n):
    if (U[i] > 1):
      return False, None
  return True, U

def UUnifast_discard (n, maxU):
  flag, U = UUnifast_discard_step(n, maxU)
  while not flag:
    flag, U = UUnifast_discard_step(n, maxU)
  return U

# Sort by criticality first, then utilization
def sort_tasks_criticality (t1, t2):
  if t1['HI'] and not t2['HI']:
    return -1
  elif not t1['HI'] and t2['HI']:
    return 1
  else:
    if t1['U'] >= t2['U']:
      return -1
    else:
      return 1

# n -> Taskset size
# p -> Percentage of HI-crit tasks
# f -> Criticality factor
# maxU -> Total taskset utilization
def generate_taskset (n, p, f, maxU, experiment_id):
  # print (n)
  U = []
  T = []
  if experiment_id == 4:
    max_armonicity = 35
  else:
    max_armonicity = 2

  config.GLOBAL_TASKSET_ID += 1
  HI_tot = n * p
  LO_tot = n - HI_tot
  t_perale = perale_taskset_generator.create_taskset_hyper_113400000_10_200_with_some_long(n, maxU, 1, max_armonicity)

  for t in t_perale[0]:
    T.append(t[2]/1000)

  # The Dirichlet Rescale (DRS) algorithm
  # https://sigbed.org/2020/12/21/the-dirichlet-rescale-drs-algorithm-a-general-purpose-method-underpinning-synthetic-task-set-generation/
  U = drs (n, maxU, [config.TASK_MAX_NOMINAL_UTILIZATION for _ in range(n)], [config.TASK_MIN_NOMINAL_UTILIZATION for _ in range(n)])
  
  # T = log_uniform(n)
  taskset = []
  for i in range(n):
    new_task = {
      'ID': i+1,
      # Is this task HI-crit?
      'HI': False,
      # HI-crit WCET
      'C(HI)': -1,
      # LO-crit WCET
      'C(LO)': -1,
      # Nominal utilization
      'U': U[i],
      # Deadline (== Period)
      'D': T[i],
      # Jitter
      'J': 0,
      # Is this task migratable?
      'migrating': False,
      # Which migration route does this task follow?
      'migration_route': [],
      # Priorities for each core
      'P': {'c1': -1, 'c2': -1}
    }
    # Randomly set tasks as HI-crit (but always respect the percentage of HI-crit tasks "p")
    HI_flag = random.choice([True, False])
    if HI_flag and HI_tot <= 0:
      HI_flag = False
    if not HI_flag and LO_tot <= 0:
      HI_flag = True
    if HI_flag:
      HI_tot -= 1
      new_task['HI'] = True
      new_task['C(HI)'] = U[i] * T[i]
      #print (new_task['C(HI)'])
      new_task['C(LO)'] = new_task['C(HI)'] / f
    else:
      new_task['C(LO)'] = U[i] * T[i]
      new_task['C(HI)'] = new_task['C(LO)'] * f
      LO_tot -= 1
    # print ("Generated task ", new_task)
    taskset.append(new_task)
  # Sort by criticality and utilization
  taskset.sort(key=functools.cmp_to_key(sort_tasks_criticality))
  for task in taskset:
    assert (task['U'] <= 1), 'Created task with utilization > 1'
    result_f = task['C(HI)'] / task['C(LO)']
    assert (math.isclose(result_f, f)), 'Something wrong with criticality factor, expected: ' + str(f) + ', found: ' + str(result_f)
  return taskset, config.GLOBAL_TASKSET_ID

def calc_total_utilization (taskset):
  result = 0
  for task in taskset:
    result += task['U']
  return result