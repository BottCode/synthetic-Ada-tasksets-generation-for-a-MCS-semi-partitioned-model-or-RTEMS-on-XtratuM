import config
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_data (results, output, x_lab):
  fig, ax = plt.subplots(figsize=(12,9))

  for approach in results:
    ax.plot([results[approach][i][0] for i in range(len(results[approach]))], [results[approach][i][1] for i in range(len(results[approach]))], label=approach)

  ax.set(xlabel=x_lab, ylabel='Proportion schedulable tasksets with at least one mig task / tasksets')
  ax.grid()
  plt.xticks()
  plt.legend()
  plt.savefig(output)
  print('\n-------\nResults saved at:\n\t ' + os.path.dirname(os.path.abspath(output)) + "\n-------\n")

def produce_results_experiment(experiment_id):
    xml_level_to_analyze = ""
    if experiment_id == 1:
        xml_level_to_analyze = 'tasksetutilization'
        x_lab = 'Utilization level'
    elif experiment_id == 2:
        xml_level_to_analyze = 'criticalityfactor'
        x_lab = 'Criticality Factor'
    elif experiment_id == 3:
        # hi-crit proportion
        xml_level_to_analyze = 'perc'
        x_lab = 'HI-CRIT task proportion'
    elif experiment_id == 4:
        xml_level_to_analyze = 'tasksetsize'
        x_lab = 'Taskset size'
    x_axis_levels = {}
    number_of_exec_for_each_level = {}
    results_to_plot = {}

    for approach in config.XML_Files[experiment_id]:
        if approach == 'nomigration':
            continue
        results_to_plot[approach] = []
        x_axis_levels[approach] = {}

        number_of_exec_for_each_level[approach] = {}
        tree = ET.parse(config.XML_Files[experiment_id][approach])
        root = tree.getroot()
        
        for taskset_XML in root.findall('taskset'):
            if int(taskset_XML.find('tasksetid').text) != -1:
                single_level = taskset_XML.find(xml_level_to_analyze).text
                
                if single_level not in number_of_exec_for_each_level[approach]:
                    number_of_exec_for_each_level[approach][single_level] = 1
                    #x_axis_levels[approach][single_level] = 0
                else:
                    number_of_exec_for_each_level[approach][single_level] += 1

        # print(number_of_exec_for_each_level)
        # print(config.STEPS*config.NUMBER_OF_TESTS)
        for level in number_of_exec_for_each_level[approach]:
            if experiment_id == 1:
                config.STEPS = 1
            # compute percentage of taskset schedulable / total taskset
            if config.STEPS * config.NUMBER_OF_TESTS == 0:
                perc = 0
            else:
                perc = (number_of_exec_for_each_level[approach][level] / (config.STEPS * config.NUMBER_OF_TESTS)) * 100

            results_to_plot[approach].append([float(level), perc])

    output_path = config.RESULTS_DIR + 'result_taskset_sched_exp_' + str(experiment_id) + '.png'
    plot_data(results_to_plot, output_path, x_lab)

# It compares the simulations result by schedulable tasksets with at least one migrating task.
def compare_simulation_focusing_only_on_schedulable_taskset():
    if config.RUN_FIRST_TEST:
        produce_results_experiment(1)
    if config.RUN_SECOND_TEST:
        produce_results_experiment(2)
    if config.RUN_THIRD_TEST:
        produce_results_experiment(3)
    if config.RUN_FOURTH_TEST:
        produce_results_experiment(4)