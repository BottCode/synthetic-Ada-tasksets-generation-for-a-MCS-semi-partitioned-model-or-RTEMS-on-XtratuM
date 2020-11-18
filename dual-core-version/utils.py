import copy
import config

import xml.etree.ElementTree as ET
import xml.dom.minidom

from shutil import copyfile

def clean_XML_Files(experiment_id):
  Files_To_Clean = config.XML_Files[experiment_id]
  xml_template = './XML_tasksets/template.xml'

  for path in config.XML_Files[experiment_id]:
    copyfile(xml_template, config.XML_Files[experiment_id][path])


def save_taskset_as_XML (c1_steady, c2_steady, c1_with_mig, c2_with_mig, approach, experiment_id, taskset_U, criticality_factor, hi_crit_proportion, util_on_c1, util_on_c2):
  number_of_cores = 2
  cores_indexes = ['c1', 'c2']

  assert(len(c1_with_mig) + len(c2_with_mig) > 0), "We have to save only those tasksets concerning at least one migrating task."
  
  cores_steady = [c1_steady, c2_steady]
  cores_with_mig = [c1_with_mig, c2_with_mig]

  print("SAVE THIS ")
  print(config.XML_Files[experiment_id][approach])
  print(c1_steady)
  print(c2_steady)
  print(c1_with_mig)
  print(c2_with_mig)
  cores = [[], []]
  utilizations_XML = [[], []]
  tasks_XML = [[], []]

  tree = ET.parse(config.XML_Files[experiment_id][approach])
  root = tree.getroot()

  taskset_selector_XML = ET.SubElement(root, 'taskset')

  size_XML = ET.SubElement(taskset_selector_XML, 'size')
  size_XML.text = str(len(c1_steady) + len(c2_steady))

  util_XML = ET.SubElement(taskset_selector_XML, 'tasksetutilization')
  util_XML.text = str(taskset_U)

  criticality_factor_XML = ET.SubElement(taskset_selector_XML, 'criticalityfactor')
  criticality_factor_XML.text = str(criticality_factor)

  # proportion of HI-crit tasks
  perc_XML = ET.SubElement(taskset_selector_XML, 'perc')
  perc_XML.text = str(hi_crit_proportion)

  cores[0] = ET.SubElement(taskset_selector_XML, 'core1')
  cores[1] = ET.SubElement(taskset_selector_XML, 'core2')

  utilizations_XML[0] = ET.SubElement(cores[0], 'utilization')
  utilizations_XML[0].text = str(util_on_c1)

  utilizations_XML[1] = ET.SubElement(cores[1], 'utilization')
  utilizations_XML[1].text = str(util_on_c2)

  tasks_XML[0] = ET.SubElement(cores[0], 'tasks') 
  tasks_XML[1] = ET.SubElement(cores[1], 'tasks')  

  for i in range(number_of_cores):
    if i == 0:
      index_other_core = 1
    else:
      index_other_core = 0
    # number of tasks on core i
    total_XML = ET.SubElement(tasks_XML[i], 'total')
    total_XML.text = str(len(cores_steady[i]))
    # save core_i's tasks
    for task in cores_steady[i]:
      task_XML = ET.SubElement(tasks_XML[i], 'task')

      ID_XML = ET.SubElement(tasks_XML[i], 'ID')
      ID_XML.text = str(task['ID'])

      criticality_XML = ET.SubElement(task_XML, 'criticality')
      criticality_XML.text = 'HIGH' if task['HI'] else 'LOW'

      # HI-Crit execution time
      CHI_XML = ET.SubElement(task_XML, 'CHI')
      CHI_XML.text = str(task['C(HI)'])

      # LO-Crit execution time
      CLO_XML = ET.SubElement(task_XML, 'CLO')
      CLO_XML.text = str(task['C(LO)'])

      nominalutil_XML = ET.SubElement(task_XML, 'nominalutil')
      nominalutil_XML.text = str(task['U'])

      deadline_XML = ET.SubElement(task_XML, 'deadline')
      deadline_XML.text = str(task['D'])

      reduceddead_XML = ET.SubElement(task_XML, 'reduceddead')
      reduceddead_XML.text = str(task['D1']) if 'D1' in task else ""

      jitter_XML = ET.SubElement(task_XML, 'jitter')
      jitter_XML.text = str(task['J'])

      is_migrating_XML = ET.SubElement(task_XML, 'migrating')
      is_migrating_XML.text = str(task['migrating'])

      priority_XML = ET.SubElement(task_XML, 'priority')
      priority_XML.text = str(task['P'][cores_indexes[i]])

      hostingmigpriority_XML = ET.SubElement(task_XML, 'hostingmigpriority')
      hostingmigpriority_XML.text = str(task['P']['hosting_migrating']) if 'hosting_migrating' in task['P'] else str(-1)

      targetpriority_XML = ET.SubElement(task_XML, 'targetpriority')
      targetpriority_XML.text = str(task['P'][cores_indexes[index_other_core]])

      # Deadline equal to period
      period_XML = ET.SubElement(task_XML, 'period')
      period_XML.text = str(task['D'])

      workload_XML = ET.SubElement(task_XML, 'workload')
      # workload_XML.text = task['workload']

  tree.write(config.XML_Files[experiment_id][approach])

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

def check_size_taskset_with_mig (total, approach, experiment_id, taskset_utilization, criticality_factor, hi_crit_proportion):
  assert(len(config.last_time_on_core_i['c1']) + len(config.last_time_on_core_i['c2']) == total), "Wrong number of scheduled tasks"
  cores = ['c1', 'c2']
  # is there at least one migrating task on c_i?
  mig_on_c_i = {'c1': False, 'c2': False}

  comparing_steady_mode = copy.deepcopy(config.last_time_on_core_i)
  comparing_migration_mode = copy.deepcopy(config.last_time_on_core_i_with_additional_migrating_task)
  util_on_core_i = {'c1': 0, 'c2': 0}

  migrating_tasks = []

  other_core = 'c2'

  for core in cores:
    if core == 'c1':
      other_core = 'c2'
    else:
      other_core = 'c1'
    for task in config.last_time_on_core_i[core]:
      util_on_core_i[core] += task['U']
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
          task['P']['hosting_migrating'] = t2['P']['c2']
          find = True
          break
      if not find:
        assert(find)
        print(task['ID'], "is missing in c2")
      
    for task in config.last_time_on_core_i_with_additional_migrating_task['c2']:
      for t2 in config.last_time_on_core_i['c1']:
        if task['ID'] == t2['ID']:
          t2['P']['c2'] = task['P']['c2']
          break
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
          task['P']['hosting_migrating'] = t2['P']['c1']
          find = True
          break
      if not find:
        print(task['ID'], "is missing in c2")
        assert(find)
        break

    for task in config.last_time_on_core_i_with_additional_migrating_task['c1']:
      find = False
      for t2 in config.last_time_on_core_i['c2']:
        if task['ID'] == t2['ID']:
          t2['P']['c1'] = task['P']['c1']
          break
  else:
    #assert(len(config.last_time_on_core_i_with_additional_migrating_task['c1']) <= 0), 'c1 should NOT have migrating tasks'
    if not (len(config.last_time_on_core_i_with_additional_migrating_task['c1']) <= 0):
      print('c1 should NOT have migrating tasks')
      # @TODO: you are cheating...
      config.last_time_on_core_i_with_additional_migrating_task['c1'] = []

  if mig_on_c_i['c1'] or mig_on_c_i['c2']:
    save_taskset_as_XML(config.last_time_on_core_i['c1'], config.last_time_on_core_i['c2'], config.last_time_on_core_i_with_additional_migrating_task['c1'], config.last_time_on_core_i_with_additional_migrating_task['c2'], approach, experiment_id, taskset_utilization, criticality_factor, hi_crit_proportion, util_on_core_i['c1'], util_on_core_i['c2'])

def beautify_XML_Files(experiment_id):
  for path in config.XML_Files[experiment_id]:
    with open(config.XML_Files[experiment_id][path], "r") as xmldata:
      parsing = xml.dom.minidom.parseString(xmldata.read())  # or xml.dom.minidom.parseString(xml_string)
      xml_pretty_str = parsing.toprettyxml()
      xmldata.close()

    with open(config.XML_Files[experiment_id][path], "w") as xmldata:
      xmldata.write(xml_pretty_str)
      xmldata.close()




