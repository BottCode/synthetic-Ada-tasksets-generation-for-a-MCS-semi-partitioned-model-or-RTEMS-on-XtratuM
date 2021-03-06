from progress.bar import Bar
from taskset import generate_taskset, calc_total_utilization
from rta import verify_no_migration, verify_model_1, verify_model_2, verify_model_3
from plot import plot_data
from joblib import Parallel, delayed
import config
import copy
import sys

def create_chart (results, x_label, y_label, filename):
  data_to_plot = []
  if config.CHECK_NO_MIGRATION:
    data_to_plot.append({'label': 'No Migration', 'data': results[0]})
  if config.CHECK_MODEL_1:
    data_to_plot.append({'label': 'Model 1', 'data': results[1]})
  if config.CHECK_MODEL_2:
    data_to_plot.append({'label': 'Model 2', 'data': results[2]})
  if config.CHECK_MODEL_3:
    data_to_plot.append({'label': 'Model 3', 'data': results[3]})
  plot_data(
    data_to_plot,
    x_label,
    y_label,
    config.RESULTS_DIR + filename)

# Run one instance of the tests (this functions is necessary for parallelism)
def run_instance (n, p, f, U):
  taskset = generate_taskset(n, p, f, U)
  # print (taskset)
  # sys.exit()
  taskset_utilization = calc_total_utilization(taskset)
  taskset_schedulability = [False, False, False, False]
  if config.CHECK_NO_MIGRATION and verify_no_migration(copy.deepcopy(taskset)):
    taskset_schedulability[0] = True
  if config.CHECK_MODEL_1 and verify_model_1(copy.deepcopy(taskset)):
    taskset_schedulability[1] = True
  if config.CHECK_MODEL_2 and verify_model_2(copy.deepcopy(taskset)):
    taskset_schedulability[2] = True
  if config.CHECK_MODEL_3 and verify_model_3(copy.deepcopy(taskset)):
    taskset_schedulability[3] = True
  return taskset_schedulability, taskset_utilization

# First test: check percentage of schedulable tasksets with different utilizations
def run_first_test ():
  res_global = [[], [], [], []]
  # Starting and final utilization values
  U = 3.2
  finish_U = 4.6
  # Utilization step
  step = 0.028
  first_test_bar = Bar('First test', max=51)
  while U <= finish_U:
    res_local = [[U, 0], [U, 0], [U, 0], [U, 0]]
    results = Parallel(n_jobs=config.PARALLEL_JOBS)(delayed(run_instance)(24, 0.5, 2, U) for _ in range(config.NUMBER_OF_TESTS))
    for result in results:
      for i in range(4):
        if result[0][i]:
          res_local[i][1] += 1
    for i in range(4):
      res_local[i][1] = res_local[i][1] * 100 / config.NUMBER_OF_TESTS
      res_global[i].append(res_local[i])
    U += step
    first_test_bar.next()
  first_test_bar.finish()
  create_chart(res_global, 'Utilization', 'Schedulable Tasksets', 'result_1.png')

# This test is similar to "run_first_test" but keeps track of total utilization vs. total schedulable utilization
# n -> Taskset size
# p -> Percentage of HI-crit tasks
# f -> Criticality factor
def check_utilization_total_schedulability (n, p, f):
  # Keep track of the sum of all tasksets' utilizations
  total_utilizations = 0
  # Keep track of the sum of schedulable tasksets' utilizations (for every model)
  total_schedulable_utilizations = [0, 0, 0, 0]
  # Starting utilization value
  U = 3.2
  # Utilization step
  step = 0.028
  while U <= 4.6:
    results = Parallel(n_jobs=config.PARALLEL_JOBS)(delayed(run_instance)(n, p, f, U) for _ in range(config.NUMBER_OF_TESTS))
    for result in results:
      for i in range(4):
        if result[0][i]:
          total_schedulable_utilizations[i] += result[1]
      total_utilizations += result[1]
    U += step
  return total_utilizations, total_schedulable_utilizations

def run_second_test ():
  res_global = [[], [], [], []]
  # Starting and final Criticality Factor values
  f = 1.25
  finish_f = 3.75
  f_step = 0.25
  second_test_bar = Bar('Second test', max=11)
  while f <= finish_f:
    total_utilizations, total_schedulable_utilizations = check_utilization_total_schedulability(24, 0.5, f)
    for i in range(4):
      res_global[i].append([f, total_schedulable_utilizations[i] / total_utilizations])
    f += f_step
    second_test_bar.next()
  second_test_bar.finish()
  create_chart(res_global, 'Criticality Factor', 'Weighted Schedulability', 'result_2.png')

def run_third_test ():
  res_global = [[], [], [], []]
  # Starting and final Proportion of HI-crit tasks values
  p = 0.1
  finish_p = 0.9
  p_step = 0.1
  third_test_bar = Bar('Third test', max=9)
  while p <= finish_p:
    total_utilizations, total_schedulable_utilizations = check_utilization_total_schedulability(24, p, 2)
    for i in range(4):
      res_global[i].append([p, total_schedulable_utilizations[i] / total_utilizations])
    p += p_step
    third_test_bar.next()
  third_test_bar.finish()
  create_chart(res_global, 'Proportion of HI-crit tasks', 'Weighted Schedulability', 'result_3.png')

def run_fourth_test ():
  res_global = [[], [], [], []]
  # Starting and final Tasksets' size values
  n = 32
  final_n = 144
  n_step = 16
  fourth_test_bar = Bar('Fourth test', max=8)
  while n <= final_n:
    total_utilizations, total_schedulable_utilizations = check_utilization_total_schedulability(n, 0.5, 2)
    for i in range(4):
      res_global[i].append([n, total_schedulable_utilizations[i] / total_utilizations])
    n += n_step
    fourth_test_bar.next()
  fourth_test_bar.finish()
  create_chart(res_global, 'Taskset size', 'Weighted Schedulability', 'result_4')

if config.RUN_FIRST_TEST:
  print('>>> Running first test')
  run_first_test()
if config.RUN_SECOND_TEST:
  print('>>> Running second test')
  run_second_test()
if config.RUN_THIRD_TEST:
  print('>>> Running third test')
  run_third_test()
if config.RUN_FOURTH_TEST:
  print('>>> Running fourth test')
  run_fourth_test()
print('>>> Done')