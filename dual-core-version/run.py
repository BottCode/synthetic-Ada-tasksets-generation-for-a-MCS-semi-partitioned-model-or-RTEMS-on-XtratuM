from progress.bar import Bar
from taskset import generate_taskset, calc_total_utilization
from rta import verify_no_migration, verify_model_1
from plot import plot_data
from joblib import Parallel, delayed
import config
import copy
import sys
import utils
import compare_schedulable_taskset
import optparse

def create_chart (results, x_label, y_label, filename):
  data_to_plot = []
  if config.CHECK_NO_MIGRATION:
    data_to_plot.append({'label': 'No Migration', 'data': results[0]})
  if config.CHECK_SEMI_1_BF:
    data_to_plot.append({'label': 'SEMI-1 BF', 'data': results[1]})
  if config.CHECK_SEMI_1_FF:
    data_to_plot.append({'label': 'SEMI-1 FF', 'data': results[2]})
  if config.CHECK_SEMI_1_WF:
    data_to_plot.append({'label': 'SEMI-1 WF', 'data': results[3]})
  if config.CHECK_SEMI_2_BF:
    data_to_plot.append({'label': 'SEMI-2 BF', 'data': results[4]})
  if config.CHECK_SEMI_2_FF:
    data_to_plot.append({'label': 'SEMI-2 FF', 'data': results[5]})
  if config.CHECK_SEMI_2_WF: 
    data_to_plot.append({'label': 'SEMI-2 WF', 'data': results[6]})

  # print(data_to_plot)
  plot_data(
    data_to_plot,
    x_label,
    y_label,
    config.RESULTS_DIR + filename)

def select_bin_packing_algorithm (selection):
  if selection == "FIRST_FIT_BP":
    config.FIRST_FIT_BP = True
    config.BEST_FIT_BP  = False
    config.WORST_FIT_BP = False
  elif selection == "WORST_FIT_BP":
    config.FIRST_FIT_BP = False
    config.BEST_FIT_BP  = False
    config.WORST_FIT_BP = True
  elif selection == "BEST_FIT_BP":
    config.FIRST_FIT_BP = False
    config.BEST_FIT_BP  = True
    config.WORST_FIT_BP = False
  else:
    # # print('!!! ERROR: No bin-packing algorithm selected !!!')
    sys.exit()

# Run one instance of the tests (this functions is necessary for parallelism)
def run_instance (n, p, f, U, experiment_id):
  # # # print("taskset: ", n, p, f, U)
  taskset, taskset_id = generate_taskset(n, p, f, U, experiment_id)
  # sys.exit()
  taskset_utilization = calc_total_utilization(taskset)

  taskset_schedulability = []
  for _ in range(config.NUMBER_OF_APPROACHES):
    taskset_schedulability.append(False)

  config.last_time_on_core_i = {'c1': [], 'c2': []}
  config.last_time_on_core_i_with_additional_migrating_task = {'c1': [], 'c2': []}

  if config.CHECK_NO_MIGRATION:
    select_bin_packing_algorithm("WORST_FIT_BP")
    if verify_no_migration(copy.deepcopy(taskset), True):
      # print("Schedulable without migration")
      utils.check_size_taskset_with_mig(n, 'nomigration', experiment_id, U, f, p, taskset_id)
      # print_XML()
      taskset_schedulability[0] = True

  fetched_approach = True
  if config.CHECK_SEMI_1_BF:
    select_bin_packing_algorithm("BEST_FIT_BP")
    T = copy.deepcopy(taskset)
    if verify_model_1(T, fetched_approach):
      # print("taskset schedulable with semi1BF")
      utils.check_size_taskset_with_mig(n, 'semi1BF', experiment_id, U, f, p, taskset_id)
      # print_XML()
      # # print(T)
      # # print("---")
      taskset_schedulability[1] = True
  
  if config.CHECK_SEMI_1_FF:
    select_bin_packing_algorithm("FIRST_FIT_BP")
    
    if verify_model_1 (copy.deepcopy(taskset), fetched_approach):
      taskset_schedulability[2] = True
      # print("Schedulable with semi1FF")
      utils.check_size_taskset_with_mig(n, 'semi1FF', experiment_id, U, f, p, taskset_id)
      # print_XML()
  
  if config.CHECK_SEMI_1_WF:
    select_bin_packing_algorithm("WORST_FIT_BP")
    
    if verify_model_1 (copy.deepcopy(taskset), fetched_approach):
      taskset_schedulability[3] = True
      # print("Schedulable with semi1WF")
      utils.check_size_taskset_with_mig(n, 'semi1WF', experiment_id, U, f, p, taskset_id)
      # print_XML()
  
  fetched_approach = False
  if config.CHECK_SEMI_2_BF:
    select_bin_packing_algorithm("BEST_FIT_BP")
    
    if verify_model_1 (copy.deepcopy(taskset), fetched_approach):
      taskset_schedulability[4] = True
      # print("Schedulable with semi2BF")
      utils.check_size_taskset_with_mig(n, 'semi2BF', experiment_id, U, f, p, taskset_id)
      # print_XML()
  
  if config.CHECK_SEMI_2_FF:
    select_bin_packing_algorithm("FIRST_FIT_BP")
    
    if verify_model_1 (copy.deepcopy(taskset), fetched_approach):
      taskset_schedulability[5] = True
      # print("Schedulable with semi2FF")
      utils.check_size_taskset_with_mig(n, 'semi2FF', experiment_id, U, f, p, taskset_id)
      # print_XML()
  
  if config.CHECK_SEMI_2_WF:
    select_bin_packing_algorithm("WORST_FIT_BP")
    
    if verify_model_1 (copy.deepcopy(taskset), fetched_approach):
      taskset_schedulability[6] = True
      # print("Schedulable with semi2WF")
      utils.check_size_taskset_with_mig(n, 'semi2WF', experiment_id, U, f, p, taskset_id)
      # print_XML()
  
  return taskset_schedulability, taskset_utilization

# First test: check percentage of schedulable tasksets with different utilizations
def run_first_test ():
  experiment_id = 1
  utils.clean_XML_and_Ada_Files(experiment_id)

  res_global = []
  for _ in range(config.NUMBER_OF_APPROACHES):
    res_global.append([])

  # Starting and final utilization values
  U = config.UTIL_LOWER_BOUND
  # Utilization step
  step = config.UTIL_STEP
  finish_U = config.UTIL_HIGHER_BOUND
  first_test_bar = Bar('First test', max=(int((finish_U-U)//step))+1)
  config.STEPS = 0
  while U <= finish_U:
    # For each utilization level

    # res_local[0] is no migration
    # res_local[1] is SEMI-1 BF 
    # res_local[2] is SEMI-1 FF
    # res_local[3] is SEMI-1 WF
    # res_local[4] is SEMI-2 BF
    # res_local[5] is SEMI-2 FF
    # res_local[6] is SEMI-2 WF
    res_local = []
    for _ in range(config.NUMBER_OF_APPROACHES):
      res_local.append([U,0])

    results = Parallel(n_jobs=config.PARALLEL_JOBS)(delayed(run_instance)(12, 0.5, 2, U, experiment_id) for _ in range(config.NUMBER_OF_TESTS))
    for result in results:
      for i in range(config.NUMBER_OF_APPROACHES):
        if result[0][i]:
          res_local[i][1] += 1
  
    for i in range(config.NUMBER_OF_APPROACHES):
      res_local[i][1] = res_local[i][1] * 100 / config.NUMBER_OF_TESTS
      res_global[i].append(res_local[i])

    U += step
    config.STEPS += 1
    first_test_bar.next()

  utils.beautify_XML_Files(experiment_id)
  utils.save_taskset_as_Ada(experiment_id)
  #utils.save_taskset_as_Ada_NO_MIG(experiment_id)
  #utils.save_taskset_as_Ada_On_RTEMS_On_XM(experiment_id)
  first_test_bar.finish()
  create_chart(res_global, 'Utilization', 'Schedulable Tasksets', 'result_1.png')

# This test is similar to "run_first_test" but keeps track of total utilization vs. total schedulable utilization
# n -> Taskset size
# p -> Percentage of HI-crit tasks
# f -> Criticality factor
def check_utilization_total_schedulability (n, p, f, experiment_id):
  # Keep track of the sum of all tasksets' utilizations
  total_utilizations = 0
  # Keep track of the sum of schedulable tasksets' utilizations (for every model)
  total_schedulable_utilizations = []
  for _ in range(config.NUMBER_OF_APPROACHES):
    total_schedulable_utilizations.append(0)
  # Starting utilization value
  U = config.UTIL_LOWER_BOUND
  # Utilization step
  step = config.UTIL_STEP
  config.STEPS = 0
  while U <= config.UTIL_HIGHER_BOUND:
    results = Parallel(n_jobs=config.PARALLEL_JOBS)(delayed(run_instance)(n, p, f, U, experiment_id) for _ in range(config.NUMBER_OF_TESTS))
    for result in results:
      for i in range(config.NUMBER_OF_APPROACHES):
        if result[0][i]:
          total_schedulable_utilizations[i] += result[1]
      total_utilizations += result[1]
    U += step
    config.STEPS += 1
  return total_utilizations, total_schedulable_utilizations

def run_second_test ():
  experiment_id = 2
  utils.clean_XML_and_Ada_Files(experiment_id)
  res_global = []
  for _ in range(config.NUMBER_OF_APPROACHES):
    res_global.append([])
  # Starting and final Criticality Factor values
  f = config.CRITICALITY_LOWER_BOUND
  finish_f = config.CRITICALITY_HIGHER_BOUND
  f_step = config.CRITICALITY_STEP
  second_test_bar = Bar('Second test', max=int((finish_f-f)//f_step)+1)
  while f <= finish_f:
    total_utilizations, total_schedulable_utilizations = check_utilization_total_schedulability(12, 0.5, f, experiment_id)
    for i in range(config.NUMBER_OF_APPROACHES):
      res_global[i].append([f, total_schedulable_utilizations[i] / total_utilizations])
    f += f_step
    second_test_bar.next()

  utils.beautify_XML_Files(experiment_id)
  utils.save_taskset_as_Ada(experiment_id)
  utils.save_taskset_as_Ada_NO_MIG(experiment_id)
  utils.save_taskset_as_Ada_On_RTEMS_On_XM(experiment_id)
  second_test_bar.finish()
  create_chart(res_global, 'Criticality Factor', 'Weighted Schedulability', 'result_2.png')

def run_third_test ():
  experiment_id = 3
  utils.clean_XML_and_Ada_Files(experiment_id)
  res_global = []
  for _ in range(config.NUMBER_OF_APPROACHES):
    res_global.append([])
  # Starting and final Proportion of HI-crit tasks values
  p = config.PROPORTION_LOWER_BOUND
  finish_p = config.PROPORTION_HIGHER_BOUND
  p_step = config.PROPORTION_STEP
  third_test_bar = Bar('Third test', max=int((finish_p-p)//p_step)+1)
  while p <= finish_p:
    total_utilizations, total_schedulable_utilizations = check_utilization_total_schedulability(12, p, 2, experiment_id)
    for i in range(config.NUMBER_OF_APPROACHES):
      res_global[i].append([p, total_schedulable_utilizations[i] / total_utilizations])
    p += p_step
    if p > 0.7 and p < 0.8:
      p = 0.8
    elif p > 0.8 and p < 0.9:
      p = 0.9
    third_test_bar.next()
  
  utils.beautify_XML_Files(experiment_id)
  utils.save_taskset_as_Ada(experiment_id)
  utils.save_taskset_as_Ada_NO_MIG(experiment_id)
  utils.save_taskset_as_Ada_On_RTEMS_On_XM(experiment_id)
  third_test_bar.finish()
  create_chart(res_global, 'Proportion of HI-crit tasks', 'Weighted Schedulability', 'result_3.png')

def run_fourth_test ():
  experiment_id = 4
  utils.clean_XML_and_Ada_Files(experiment_id)
  res_global = []
  for _ in range(config.NUMBER_OF_APPROACHES):
    res_global.append([])
  # Taskset sizes
  sizes = config.TASKSETS_SIZE
  fourth_test_bar = Bar('Fourth test', max=len(sizes))
  for size in sizes:
    total_utilizations, total_schedulable_utilizations = check_utilization_total_schedulability(size, 0.5, 2, experiment_id)
    for i in range(config.NUMBER_OF_APPROACHES):
      res_global[i].append([size, total_schedulable_utilizations[i] / total_utilizations])
    fourth_test_bar.next()
  
  utils.beautify_XML_Files(experiment_id)
  utils.save_taskset_as_Ada(experiment_id)
  utils.save_taskset_as_Ada_NO_MIG(experiment_id)
  utils.save_taskset_as_Ada_On_RTEMS_On_XM(experiment_id)
  fourth_test_bar.finish()
  create_chart(res_global, 'Taskset size', 'Weighted Schedulability', 'result_4')

def parse_options():
  parser = optparse.OptionParser()

  parser.add_option('--runtime-dir',
      action="store", dest="runtimedir",
      help="query string", default="")

  parser.add_option('--runtime-nomig-dir',
      action="store", dest="runtimenomigdir",
      help="query string", default="")

  parser.add_option('--util-low',
      action="store", dest="utillow",
      help="query string", default="1.6")

  parser.add_option('--util-high',
      action="store", dest="utilhigh",
      help="query string", default="1.2")

  parser.add_option('--util-step',
      action="store", dest="utilstep",
      help="query string", default="0.012")

  parser.add_option('--criticality-low',
      action="store", dest="criticalitylow",
      help="query string", default="1.5")

  parser.add_option('--criticality-high',
      action="store", dest="criticalityhigh",
      help="query string", default="4")

  parser.add_option('--criticality-step',
      action="store", dest="criticalitystep",
      help="query string", default="0.25")

  parser.add_option('--proportion-low',
      action="store", dest="proportionlow",
      help="query string", default="0.1")

  parser.add_option('--proportion-high',
      action="store", dest="proportionhigh",
      help="query string", default="0.9")

  parser.add_option('--proportion-step',
      action="store", dest="proportionstep",
      help="query string", default="0.1")

  parser.add_option('--exp-1',
      action="store", dest="exp1",
      help="query string", default="False")

  parser.add_option('--exp-2',
      action="store", dest="exp2",
      help="query string", default="False")

  parser.add_option('--exp-3',
      action="store", dest="exp3",
      help="query string", default="False")

  parser.add_option('--exp-4',
      action="store", dest="exp4",
      help="query string", default="False")
  
  parser.add_option('--numb-tests',
      action="store", dest="numbtests",
      help="query string", default="100")
      
  options, args = parser.parse_args()
  # print(options, args)

  config.RUNTIME_DIR = '"' + options.runtimedir + '"'
  config.RUNTIME_NO_MIG_DIR = '"' + options.runtimenomigdir + '"'
  config.UTIL_STEP = float(options.utilstep)
  config.UTIL_LOWER_BOUND = float(options.utillow)
  config.UTIL_HIGHER_BOUND = float(options.utilhigh)
  config.CRITICALITY_STEP = float(options.criticalitystep)
  config.CRITICALITY_LOWER_BOUND =float (options.criticalitylow)
  config.CRITICALITY_HIGHER_BOUND = float(options.criticalityhigh)
  config.PROPORTION_STEP = float(options.proportionstep)
  config.PROPORTION_LOWER_BOUND = float(options.proportionlow)
  config.PROPORTION_HIGHER_BOUND = float(options.proportionhigh)
  config.RUN_FIRST_TEST = True if (str(options.exp1) == 'True') else False
  config.RUN_SECOND_TEST = True if (str(options.exp2) == 'True') else False
  config.RUN_THIRD_TEST = True if (str(options.exp3) == 'True') else False
  config.RUN_FOURTH_TEST = True if (str(options.exp4) == 'True') else False
  config.NUMBER_OF_TESTS = int(options.numbtests)
  #config.TASKSETS_SIZE = 


######### START ###########

parse_options()

if config.RUN_FIRST_TEST:
  # print('>>> Running first test')
  run_first_test()
  compare_schedulable_taskset.produce_results_experiment (1)
if config.RUN_SECOND_TEST:
  # print('>>> Running second test')
  run_second_test()
  compare_schedulable_taskset.produce_results_experiment (2)
if config.RUN_THIRD_TEST:
  # print('>>> Running third test')
  run_third_test()
  compare_schedulable_taskset.produce_results_experiment (3)
if config.RUN_FOURTH_TEST:
  # print('>>> Running fourth test')
  run_fourth_test()
  compare_schedulable_taskset.produce_results_experiment (4)
# print('>>> Done')

config.RUNTIME_DIR = ""