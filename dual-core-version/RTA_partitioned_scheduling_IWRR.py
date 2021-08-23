import config
import os
import shutil
import math
import utils
import random
import itertools

import xml.etree.ElementTree as ET
import xml.dom.minidom

fake_system = {'c1': {'HIGH': [
    {'ID': 7, 'HI': True, 'C(HI)': 18, 'C(LO)': 10.046999159126875, 'U': 0.14175660189244269, 'D': 42, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 1, 'c2': -1}, 'Ri': 18}, 
    {'ID': 5, 'HI': True, 'C(HI)': 15, 'C(LO)': 8.767037350015986, 'U': 0.15585844177806196, 'D': 36, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 2, 'c2': -1}, 'Ri': 15}, 
    {'ID': 4, 'HI': True, 'C(HI)': 9, 'C(LO)': 9.905537284965671, 'U': 0.19566493402401325, 'D': 30, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 3, 'c2': -1}, 'Ri' : 9}], 'LOW': [{'ID': 3, 'HI': False, 'C(HI)': 58.67644787211147, 'C(LO)': 29.338223936055734, 'U': 0.3104573961487379, 'D': 94.5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 1, 'c2': -1}, 'Ri': 37.72582202647289}, {'ID': 2, 'HI': False, 'C(HI)': 16.77519618083431, 'C(LO)': 8.387598090417155, 'U': 0.11183464120556208, 'D': 75.0, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 2, 'c2': -1}, 'Ri': 8.387598090417155}]}}

fake_scheduling_plan = {'c1': {'LOW': {'U': 0.3554248798402419, 'S': 16, 'W': 8}, 'HIGH': {'U': 0.5689675603354601, 'S': 26, 'W': 13}, 'slot_size': 6, 'IWRR_list': ['HIGH', 'LOW', 'HIGH', 'LOW', 'HIGH', 'LOW', 'LOW', 'LOW']}}

##############
# verify_schedulability
##############
def verify_schedulability (taskset, experiment_id, criticality_factor, hi_crit_proportion):
    
    high_crit_tasks   = []
    low_crit_tasks  = []
    system_util = 0
    system_size = 0

    system = {
        'c1': 
        {
            'HIGH': [], 'LOW': []
        },
        'c2': 
        {
            'HIGH': [], 'LOW': []
        }
    }

    for task in taskset:
        if task['HI']:
            high_crit_tasks.append (task)
        else:
            low_crit_tasks.append (task)

    # partitioning high critical tasks on two cores s.t. the load
    # on each core is as close as possible to the other one.
    # The partitioning algorithm is explained here: https://stackoverflow.com/a/12471974/5994681

    high_crit_tasks = sorted (high_crit_tasks, key=lambda k: k['U'], reverse = True)
    low_crit_tasks = sorted (low_crit_tasks, key=lambda k: k['U'], reverse = True)

    for task in high_crit_tasks:
        load_c1 = sum (hi_task['U'] for hi_task in system['c1']['HIGH'])
        load_c2 = sum (hi_task['U'] for hi_task in system['c2']['HIGH'])

        if load_c1 <= load_c2:
            system['c1']['HIGH'].append (task)
        else:
            system['c2']['HIGH'].append (task)

    for task in low_crit_tasks:
        load_c1 = sum (lo_task['U'] for lo_task in system['c1']['LOW'])
        load_c2 = sum (lo_task['U'] for lo_task in system['c2']['LOW'])

        if load_c1 <= load_c2:
            system['c1']['LOW'].append (task)
        else:
            system['c2']['LOW'].append (task)

    assert (len (system['c1']['LOW']) + len (system['c2']['LOW']) + len (system['c1']['HIGH']) + len (system['c2']['HIGH']) == len (taskset))

    # print (str (sum (lo_task['U'] for lo_task in system['c1']['LOW'])) + " vs " + str (sum (lo_task['U'] for lo_task in system['c2']['LOW'])) + " = " + str (abs (sum (lo_task['U'] for lo_task in system['c1']['LOW']) - sum (lo_task['U'] for lo_task in system['c2']['LOW']))))
    # print (str (sum (hi_task['U'] for hi_task in system['c1']['HIGH'])) + " vs " + str (sum (hi_task['U'] for hi_task in system['c2']['HIGH'])) + " = " + str (abs (sum (lo_task['U'] for lo_task in system['c1']['LOW']) - sum (lo_task['U'] for lo_task in system['c2']['LOW']))))

    # assign priorities according to RM

    for core in system:
        for partition in system[core]:
            system[core][partition] = sorted (system[core][partition], key=lambda k: k['D'], reverse = True)
            current_priority = 1
            for task in system[core][partition]:
                task['P'][core] = current_priority
                current_priority = current_priority + 1
                system_util += task['U']
                system_size += 1

    system_util = format (system_util, ".3f")

    is_schedulable, scheduling_plan = RTA_partitioned_scheduling (system, experiment_id)
    
    if is_schedulable:
        save_as_XML (system, scheduling_plan, experiment_id, system_util, system_size, criticality_factor, hi_crit_proportion)
    
    return is_schedulable

##############
# compute_scheduling_plan
##############
def compute_scheduling_plan (system):
    # Q: How the scheduling plan is generated?
    # A: <https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/13#note_594713546>
    system_plan = {
        'c1': {
            'LOW': {'U': 0, 'S': 0, 'W': 0},
            'HIGH': {'U': 0, 'S': 0, 'W': 0},
            'slot_size': 0,
            'IWRR_list': []
        },
        'c2': {
            'LOW': {'U': 0, 'S': 0, 'W': 0},
            'HIGH': {'U': 0, 'S': 0, 'W': 0},
            'slot_size': 0,
            'IWRR_list': []
        }
    }

    for core in system:
        # compute utilizations of both partitions on current core
        for partition in system[core]:
            system_plan[core][partition]['U'] = sum (task['U'] for task in system[core][partition])
                    
        PHI = system_plan[core]['LOW']['U'] / system_plan[core]['HIGH']['U']
        BTS = min (min (task['D'] for task in system[core]['LOW']), min (task['D'] for task in system[core]['HIGH']))

        if PHI > 1:
            # In XtratuM, the time slice width is expressed with an integer number (milliseconds).
            # This tasksets generator script generate periods of type float. That's why we use math.ceil. 
            system_plan[core]['LOW']['S'] = math.ceil (BTS)
            system_plan[core]['HIGH']['S'] = math.ceil (BTS / PHI)
        else:
            system_plan[core]['LOW']['S'] = math.ceil (BTS * PHI)
            system_plan[core]['HIGH']['S'] = math.ceil (BTS)
        
        system_plan[core]['slot_size'] = math.gcd (system_plan[core]['HIGH']['S'], system_plan[core]['LOW']['S'])
        config.gcds.append (system_plan[core]['slot_size'])
        # print ("\n", system_plan[core]['slot_size'], "gcd of", system_plan[core]['HIGH']['S'], system_plan[core]['LOW']['S'], "\n")

        for partition in system[core]:
            system_plan[core][partition]['W'] = math.ceil (system_plan[core][partition]['S'] / system_plan[core]['slot_size'])

    # Populate IWRR list, i.e. the effective scheduling plan.
    # Convention: the first partition to be scheduled is the lightest one.
    # print("\n", system_plan)
    for core in system_plan:
        W_LOW = system_plan[core]['LOW']['W']
        W_HIGH = system_plan[core]['HIGH']['W']
        next_partition_to_allocate = 'HIGH' if W_HIGH <= W_LOW else 'LOW'
        while W_LOW > 0 or W_HIGH > 0:
            if next_partition_to_allocate == 'HIGH':
                if W_HIGH > 0:
                    system_plan[core]['IWRR_list'].append ('HIGH')
                    W_HIGH = W_HIGH - 1
                next_partition_to_allocate = 'LOW'
            else:
                if W_LOW > 0:
                    system_plan[core]['IWRR_list'].append ('LOW')
                    W_LOW = W_LOW - 1
                next_partition_to_allocate = 'HIGH'
        assert len (system_plan[core]['IWRR_list']) == (system_plan[core]['LOW']['W'] + system_plan[core]['HIGH']['W']), "AssertionError on system_plan[core]['IWRR_list']"
        config.iwrr_list_lens.append (len (system_plan[core]['IWRR_list']))

        if config.iwrr_list_max_len < len (system_plan[core]['IWRR_list']):
            config.iwrr_list_max_len = len (system_plan[core]['IWRR_list'])
            print ("\n New max: s_" + str (config.GLOBAL_TASKSET_ID)+ " -> " + str (len (system_plan[core]['IWRR_list'])))

    return system_plan

##############
# RTA_partitioned_scheduling
##############
def RTA_partitioned_scheduling (system, experiment_id):

    #####
    # create MAST txt files and the overall system directory
    #####

    # system_path = to_mast_file  (system, experiment_id)

    #####
    # generate partitions' scheduling plans according to the Interleaved WRR
    # and the following strategy: <https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/13#note_594713546> 
    #####
    # print_system (system)
    scheduling_plan = compute_scheduling_plan (system)

    #####
    # analyze the overall system, i.e. check the schedulability
    # of both partitions on both core
    #####
    # system = fake_system
    # scheduling_plan = fake_scheduling_plan
    is_schedulable = analyze_system (system, scheduling_plan)
    
    '''print("##########")
    print (system)
    print ("\n")
    print (scheduling_plan)
    print("##########")'''
    if is_schedulable:
        return True, scheduling_plan

    return False, None

##############
# analyze_system
##############
def analyze_system (system, scheduling_plan):
    # for each partition, verify if its inner tasks are schedulable according to RTA for Fixed Priority scheduling.
    are_partitions_schedulable = check_inner_partition_schedulability (system)
    # print ("RTA: ", are_partitions_schedulable)
    # if so, the check the partion scheduling
    if are_partitions_schedulable:
        return check_intra_partition_scheduling (system, scheduling_plan)
    else:
        return False

def check_intra_partition_scheduling (system, scheduling_plan):
    for core in system:
        most_loaded_partition = 'HIGH' if scheduling_plan[core]['HIGH']['W'] > scheduling_plan[core]['LOW']['W'] else 'LOW'
        for partition in system[core]:
            scheduling_plan_starting_from_critical_instant = scheduling_plan[core]['IWRR_list'] if partition == most_loaded_partition else list (reversed (scheduling_plan[core]['IWRR_list']))
            for task in system[core][partition]:
                time_passed = 0
                response_time = task['Ri']
                for minor_frame in itertools.cycle (scheduling_plan_starting_from_critical_instant):
                    diff = 0
                    if minor_frame == partition:
                        if response_time >= scheduling_plan[core]['slot_size']:
                            response_time -= scheduling_plan[core]['slot_size']
                        else:
                            diff = scheduling_plan[core]['slot_size'] - response_time
                            response_time = 0
                    time_passed += scheduling_plan[core]['slot_size'] if diff == 0 else diff
                    task['PS_Ri'] = time_passed
                    if time_passed > task['D']:
                        # print ("\nOUCH!!", time_passed, task)
                        # print ("PS:", False)
                        return False
                    if response_time <= 0:
                        # this task is schedulable on partitioned scheduling!
                        break
    # print ("PS:", True)
    return True

def check_inner_partition_schedulability (system):
    for core in system:
        for partition in system[core]:
            for task in system[core][partition]:
                # select tasks with priority higher than the current one
                higher_priority_tasks = list (filter (lambda t: t['P'][core] > task['P'][core], system[core][partition]))
                # print_hp (task['P'][core], higher_priority_tasks)
                # task['Ri'] = task['C(HI)'] if task['HI'] else task['C(LO)']
                task['Ri'] = calcRi (task, higher_priority_tasks)
                if task['Ri'] == None:
                    return False
                
    return True

def calcRi (task, hp):
  start_Ri = task['C(HI)']
  Ri = start_Ri
  while True:
    newRi = start_Ri
    for hp_task in hp:
      hp_C = hp_task['C(HI)']
      newRi += math.ceil(Ri / hp_task['D']) * hp_C
    if newRi > task['D']:
      return None
    if newRi == Ri:
      return newRi
    Ri = newRi

##############
# to_mast_file
##############
def to_mast_file (system, experiment_id):

    system_dir_path = config.MAST_analysis_path[experiment_id] + "system_" + str (config.GLOBAL_TASKSET_ID)
    os.mkdir (system_dir_path)

    for core in system:

        other_partition = 'LOW'
        for partition in system[core]:

            if partition == 'LOW':
                other_partition = 'HIGH'

            file_name = "t_" + str (config.GLOBAL_TASKSET_ID) + "_" + core + "_" + partition + ".txt"
            file_path = system_dir_path + "/" + file_name

            MAST_text = ""
            MAST_text += "-- https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/13\n\n"
            MAST_text += "Model (\n" + "\tModel_Name\t=>\t" + core + partition + str (config.GLOBAL_TASKSET_ID) + ",\n\tModel_Date\t=>\t2021-07-10);\n\n"

            MAST_text += "Processing_Resource (\n\tType\t=>\tFixed_Priority_Processor,\n\tName\t=>\tCPU);\n\n"

            for task in system[core][partition]:
                MAST_text += "----------\n"
                MAST_text += "-- TASK " + str (task['ID']) + "\n"
                MAST_text += "----------\n\n"

                MAST_text += "-- Scheduling Server\n\n"

                MAST_text += "Scheduling_Server (\n\tType\t=>\tFixed_Priority,\n\tName\t=>\ttask" + str (task['ID']) +",\n"
                MAST_text += "\tServer_Sched_Parameters\t=>\t(\n\t\tType\t=>\tFixed_Priority_Policy,\n\t\tThe_Priority\t=>\t" + str (task['P'][core]) + ",\n\t\tPreassigned\t=>\tNo),\n"
                MAST_text += "\tServer_Processing_Resource\t=>\tCPU);\n\n"

                MAST_text += "-- Operation\n\n"
                WCET = str (task['C(LO)'] if partition == "LOW" else task['C(HI)'])
                MAST_text += "Operation (\n\tType\t=>\tSimple,\n\tName\t=>\toperation_task" + str (task['ID']) +",\n" + "\tWorst_Case_Execution_Time\t=>\t\t" + WCET + ");\n\n"

                MAST_text += "-- MAST Transaction\n\n"
                MAST_text += "Transaction (\n\tType\t=>\tRegular,\n\tName\t=>\ttransaction_task" + str (task['ID']) + ",\n\tExternal_Events\t=> (\n"
                MAST_text += "\t\t(Type\t=>\tPeriodic,\n\t\tName\t=>\tevent_task" + str (task['ID']) + ",\n\t\tPeriod\t=>\t" + str(task['D']) + ")\n\t),\n"
                MAST_text += "\tInternal_Events\t=> (\n\t\t(Type\t=>\tregular,\n\t\tName\t=>\tevent_out_task" + str (task['ID']) + ",\n"
                MAST_text += "\t\tTiming_Requirements\t=> (\n\t\t\tType\t=>\tHard_Global_Deadline,\n\t\t\tDeadline\t=>\t" + str (task['D']) + ",\n\t\t\tReferenced_Event\t=>\tevent_task" + str (task['ID']) + "\n\t\t))\n\t),\n"
                MAST_text += "\tEvent_Handlers\t=> (\n\t\t(Type\t=>\tActivity,\n\t\tInput_Event\t=>\tevent_task" + str (task['ID']) + ",\n\t\tOutput_Event\t=> event_out_task" + str (task['ID']) + ",\n"
                MAST_text += "\t\tActivity_Operation\t=>\toperation_task" + str (task['ID']) + ",\n\t\tActivity_Server\t=>\ttask" + str (task['ID']) + ")\n\t)\n);\n"

                # print (MAST_text, "\n")

                # MAST_text += ""

            with open(file_path, 'w') as write_obj:
                write_obj.write(MAST_text)
                write_obj.close()

    return system_dir_path
            
##############
# print_system
##############
def print_system (system):
    for core in system:
        print ("Core", core)
        for partition in system[core]:
            print("\tPartition", partition) 
            for task in system[core][partition]:
                print ("\t\ttask", task)

##############
# print_scheduling_plan
##############
def print_scheduling_plan (scheduling_plan):
    for core in scheduling_plan:
        print ("\nScheduling plan on core", core)
        print ("\tslot size:", scheduling_plan[core]['slot_size'])
        for partition in ['LOW', 'HIGH']:
            print("\tPartition Weight", partition, "=", scheduling_plan[core][partition]['W'])
        
        print ("\tScheduling plan:", scheduling_plan[core]['IWRR_list'])

##############
# save_as_XML
##############
def save_as_XML (system, scheduling_plan, experiment_id, system_util, system_size, criticality_factor, hi_crit_proportion):
    # print_system (system)
    # print_scheduling_plan (scheduling_plan)
    system_id = "s_" + str (config.GLOBAL_TASKSET_ID)
    approach = 'MAST_IWRR'
    system_size = 0
    system_util = 0

    for core in system:
        for partition in system[core]:
            for task in system[core][partition]:
                system_size += 1
                system_util += task['U']
    
    system_util = format (system_util, '.3f')

    tree = ET.parse (config.XML_Files[experiment_id][approach])
    root = tree.getroot()

    system_selector_XML = ET.SubElement(root, 'system')
    
    systemid_XML = ET.SubElement(system_selector_XML, 'systemid')
    systemid_XML.text = str(system_id)

    executionid_XML = ET.SubElement(system_selector_XML, 'executionid')
    executionid_XML.text = ('E' + str(experiment_id) + '_' + approach + '_T' + str(system_id)).lower()

    size_XML = ET.SubElement(system_selector_XML, 'systemsize')
    size_XML.text = str(system_size)

    util_XML = ET.SubElement(system_selector_XML, 'systemutilization')
    util_XML.text = str(system_util)

    criticality_factor_XML = ET.SubElement(system_selector_XML, 'criticalityfactor')
    criticality_factor_XML.text = str(criticality_factor)

    # proportion of HI-crit tasks
    perc_XML = ET.SubElement(system_selector_XML, 'perc')
    perc_XML.text = str(hi_crit_proportion)

    # print("\n", scheduling_plan, "\n")
    # print("\n", system, "\n\n")

    for core in system:
        current_core_XML = ET.SubElement (system_selector_XML, 'core', {'id': core})
        scheduling_plan_XML = ET.SubElement (current_core_XML, 'plan', {'slotwidth': str (scheduling_plan[core]['slot_size'])})

        for frame in scheduling_plan[core]['IWRR_list']:
            frame_XML = ET.SubElement (scheduling_plan_XML, 'frame', {'partition': frame})
        
        for partition in system[core]:
            current_partition_XML = ET.SubElement (current_core_XML, 'partition', {'level': partition})
            
            weight_XML = ET.SubElement (current_partition_XML, 'weight')
            weight_XML.text = str (scheduling_plan[core][partition]['W'])
            
            partition_util_XML = ET.SubElement (current_partition_XML, 'partitionutil')
            partition_util_XML.text = str (scheduling_plan[core][partition]['U'])

            partition_size_XML = ET.SubElement (current_partition_XML, 'partitionsize')
            partition_size_XML.text = str (len (system[core][partition]))

            partition_tasks_XML = ET.SubElement (current_partition_XML, 'tasks')

            for task in system[core][partition]:
                task_XML = ET.SubElement (partition_tasks_XML, 'task')

                ID_XML = ET.SubElement(task_XML, 'ID')
                ID_XML.text = str(task['ID'])

                execution_time_XML = ET.SubElement(task_XML, 'executiontime')
                execution_time_XML.text = str (task['C(LO)'] if partition == 'LOW' else task['C(HI)'])

                nominalutil_XML = ET.SubElement(task_XML, 'nominalutil')
                nominalutil_XML.text = str(task['U'])

                deadline_XML = ET.SubElement(task_XML, 'deadline')
                deadline_XML.text = str(task['D'])

                priority_XML = ET.SubElement(task_XML, 'priority')
                priority_XML.text = str((task['P'][core]))

                # Deadline equal to period
                period_XML = ET.SubElement(task_XML, 'period')
                period_XML.text = str(task['D'])

                workload_XML = ET.SubElement(task_XML, 'workload')        

    tree.write(config.XML_Files[experiment_id][approach])

def save_taskset_as_Ada_On_RTEMS_On_XM (experiment_id):
    approach = 'MAST_IWRR'
    partitions = ['HIGH', 'LOW']
    cores = ['c1', 'c2']
    common_folder = config.Ada_RTEMS_Common_Folder
    major_frames = {'c1': 0, 'c2': 0}
    slot_duration = {'c1': 0, 'c2': 0}
    IWRR_lists = {'c1': [], 'c2': []}

    tree = ET.parse(config.XML_Files[experiment_id][approach])
    root = tree.getroot()

    for system in root.findall('system'):
        periods = {'c1': {}, 'c2': {}}
        hyperperiods = {'c1': {}, 'c2': {}}
        system_id = system.find ('systemid').text

        for core in cores:
            for partition in partitions:
                periods[core][partition] = []
                hyperperiods[core][partition] = 0

        system_dir = config.Ada_RTEMS_XM_Paths[experiment_id][approach] + system_id + '/'
        os.mkdir(system_dir)
    
        Ada_Units = {}
        Ada_Units_Files_Name = {}
        Ada_SOP_Specs = {}
        Ada_SOP_Body = {}
        Single_Execution_Data = {}
        Mains_Files_Name = {}
        Main_Units = {}
        Tasksets_Name = {}
        Srcs_Dir = {}
        Apps_Dir = {}

        for core in cores:
          # XPath query
          current_core_XML = system.find ("core/[@id='" + core + "']")
          slot_duration[core] = int (current_core_XML.find ("plan").attrib['slotwidth'])

          # Get scheduling plan for current core
          for frame in current_core_XML.find ('plan').findall ('frame'):
              IWRR_lists[core].append (frame.attrib['partition'])
          
          major_frames[core] = len (IWRR_lists[core]) * slot_duration[core]

          Ada_Units[core] = {}
          Ada_Units_Files_Name[core] = {}
          Ada_SOP_Specs[core] = {}
          Ada_SOP_Body[core] = {}
          Single_Execution_Data[core] = {}
          Mains_Files_Name[core] = {}
          Main_Units[core] = {}
          Tasksets_Name[core] = {}
          Srcs_Dir[core] = {}
          Apps_Dir[core] = {}


          for partition in partitions:
            current_partition_XML = current_core_XML.find ("partition/[@level='" + partition + "']")

            Ada_Units[core][partition] = ''
            Ada_SOP_Specs[core][partition] = ''
            Ada_SOP_Body[core][partition] = ''
            Single_Execution_Data[core][partition] = ''
            Main_Units[core][partition] = ''
            Mains_Files_Name[core][partition] = ''

            Ada_Units_Files_Name[core][partition] = 'taskset_' + system_id + '_' + core + partition + '.ads'
            Tasksets_Name[core][partition] = 'taskset_' + system_id + '_' + core + partition

            Srcs_Dir[core][partition] = system_dir + core + partition + '/'
            Apps_Dir[core][partition] = Srcs_Dir[core][partition] + 'app/'
            #print (Apps_Dir)

            os.mkdir(Srcs_Dir[core][partition])
            os.mkdir(Apps_Dir[core][partition])

            # Mains generation, one for each partition 
            Main_Units[core][partition] = 'main_' + Tasksets_Name[core][partition]
            Mains_Files_Name[core][partition] = Main_Units[core][partition] + '.adb'
            main = 'with System;\nwith Periodic_Tasks;\n\n'
            main += 'procedure ' + Main_Units[core][partition] + ' is\n'
            main += "\tpragma Priority (System.Priority'Last);\n"
            main += 'begin\n\tPeriodic_Tasks.Init;\nend ' + Main_Units[core][partition] + ';'

            # create main unit Ada file
            f = open(Apps_Dir[core][partition] + Mains_Files_Name[core][partition], 'w')
            f.write(main)
            f.close()

            Ada_Units[core][partition] = 'with Ada.Real_Time; use Ada.Real_Time;\n\nwith Ada.Text_IO;\n\nwith System.Multiprocessors;\nuse System.Multiprocessors;\n\n'
            Ada_Units[core][partition] += 'with Single_Execution_Data;\nwith Production_Workload;\nwith Set_Of_Procedures;\nwith Workload_Manager;\nwith Initial_Delay;\n\nwith RTEMS;\nwith RTEMS.TASKS;\nwith RTEMS.CPU_Usage;\n\n'
            # Ada_Units[core][partition] += 'use Periodic_Tasks;\n\npackage taskset_' + Tasksets_Name[core][partition] + ' is\n\n'
            Ada_Units[core][partition] += 'package body Periodic_Tasks is\n\n'
            Ada_Units[core][partition] += '\tfunction Get_Longest_Hyperperiod return Natural is\n\t\tMax_H : Natural := Single_Execution_Data.Experiment_Hyperperiods(1);\n\tbegin\n'
            Ada_Units[core][partition] += '\t\tfor I in Single_Execution_Data.Experiment_Hyperperiods\'Range loop\n'
            Ada_Units[core][partition] += '\t\t\tif Single_Execution_Data.Experiment_Hyperperiods(I) > Max_H then\n\t\t\t\tMax_H := Single_Execution_Data.Experiment_Hyperperiods(I);\n\t\t\tend if;\n\t\tend loop;\n\n'
            Ada_Units[core][partition] += '\t\treturn Max_H;\n\t end Get_Longest_Hyperperiod;\n\n'
            Ada_Units[core][partition] += '\t------------\n\t--  Init  --\n\t------------\n\n'
            Ada_Units[core][partition] += '\tprocedure Init is\n\t\tNext_Period : constant Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);\n\t\tPeriod_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod);\n\n'

            Ada_SOP_Specs[core][partition] += 'with RTEMS.TASKS;\n\npackage Set_Of_Procedures is\n\n'
            Ada_SOP_Body[core][partition] += 'with Ada.Real_Time; use Ada.Real_Time;\n\nwith Single_Execution_Data;\nwith Production_Workload;\nwith Workload_Manager;\nwith Initial_Delay;\n\nwith Ada.Text_IO;\n\n'
            Ada_SOP_Body[core][partition] += 'package body Set_Of_Procedures is\n\n\tprocedure Work (Period : Duration; ID : Natural);\n\tpragma No_Return (Work);\n\n'
            Ada_SOP_Body[core][partition] += '\tprocedure Work (Period : Duration; ID : Natural) is\n'
            Ada_SOP_Body[core][partition] += '\t\t--  Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);\n\t\t--  Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Period);\n\t\tI : Natural := 0;\n'
            Ada_SOP_Body[core][partition] += '\t\tFake_Status : RTEMS.STATUS_CODES;\n\t\tFake_Previous_Mode : RTEMS.MODE;\t\tDelayed_At : Ada.Real_Time.Time;\n\t\tWaked_At : Ada.Real_Time.Time;\n\t\tDeadline : Ada.Real_Time.Time;\n\t\tTime_To_Sleep : Duration := 0.0;\n\t\tNow : Ada.Real_Time.Time;\n'
            # Ada_SOP_Body[core][partition] += '\tbegin\n\t\tloop\n\t\t\tdelay until Next_Period;\n\n\t\t\tProduction_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));\n\n\t\t\tI := I + 1;\n\n\t\t\tNext_Period := Next_Period + Period_To_Add;\n\t\tend loop;\n\tend Work;\n\n'
            Ada_SOP_Body[core][partition] += '\tbegin\n\n\t\tdelay 2.0;\n\n\t\tloop\n\t\t\tDeadline := Ada.Real_Time.Clock + To_Time_Span (Period);\n\n\t\t\tProduction_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));\n\n\t\t\tI := I + 1;\n\n\t\t\tNow := Ada.Real_Time.Clock;\n\n\t\t\tif Now <= Deadline then\n\n\t\t\t\tRTEMS.TASKS.MODE (RTEMS.NO_PREEMPT, 0, Fake_Previous_Mode, Fake_Status);\n\n\t\t\t\tTime_To_Sleep := To_Duration (Deadline - Ada.Real_Time.Clock);\n\t\t\t\t--  Delayed_At := Ada.Real_Time.Clock;\n\t\t\t\tdelay Time_To_Sleep;\n\t\t\t\t--  Waked_At := Ada.Real_Time.Clock;\n\n\t\t\t\tRTEMS.TASKS.MODE (RTEMS.PREEMPT, 0, Fake_Previous_Mode, Fake_Status);\n\t\t\t\t--  Ada.Text_IO.Put_Line ("Error Task " & Natural\'Image (ID) & ": " & Duration\'Image (Abs (Time_To_Sleep - (To_Duration (Waked_At - Delayed_At))) * 1_000) & " milliseconds");\n'
            Ada_SOP_Body[core][partition] += '\n\t\t\telse\n\t\t\t\t-- Ada.Text_IO.Put_Line ("DM Task " & Natural\'Image (ID));\n\t\t\t\tIs_Valid := False;\n\t\t\tend if;\n\t\tend loop;\n\tend Work;\n\n'

            tasks_on_current_partition_XML = current_partition_XML.find('tasks')
            for task in tasks_on_current_partition_XML.findall('task'):
                # print (task.find('ID').text)
            
                Ada_Units[core][partition] += '\t\tID_T_' + str(task.find('ID').text) + ' : RTEMS.ID;\n'
                Ada_Units[core][partition] += '\t\tSTATUS_T_' + str(task.find('ID').text) + ' : RTEMS.STATUS_CODES;\n'

                Ada_SOP_Specs[core][partition] += '\tprocedure T_' + str(task.find('ID').text) + '_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);\n'
                Ada_SOP_Specs[core][partition] += '\tpragma Convention (C, T_' + str(task.find('ID').text) + '_Body);\n\n'

                Ada_SOP_Body[core][partition] += '\tprocedure T_' + str(task.find('ID').text) + '_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is\n\t\tpragma Unreferenced (ARGUMENT);\n\t\tPeriod : Duration := ' + str((utils.to_microseconds_for_Ada (task.find('period').text)) / 1000000) + ';\n'
                Ada_SOP_Body[core][partition] += '\t\tID : Natural := ' + str(task.find('ID').text) + ';\n'
                Ada_SOP_Body[core][partition] += '\tbegin\n\t\tWork (Period, ID);\n\tend T_' + str(task.find('ID').text) + '_Body;\n\n'

                periods[core][partition].append (int(utils.to_microseconds_for_Ada (task.find('period').text)))

            Ada_Units[core][partition] += '\n\t\tID_T_LAST : RTEMS.ID;\n\t\tSTATUS_T_LAST : RTEMS.STATUS_CODES;\n\tbegin\n\n'
            Ada_SOP_Specs[core][partition] += '\tprocedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT);\n'
            Ada_SOP_Specs[core][partition] += '\tpragma Convention (C, LAST);\n\n'
            Ada_SOP_Specs[core][partition] += '\t-- True iff no deadlines are missed.\n\tIs_Valid : Boolean := True;\n\nend Set_Of_Procedures;\n\n'
            # Ada_SOP_Body[core][partition] += '\tprocedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is\n\t\tpragma Unreferenced (ARGUMENT);\n\t\tNext_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Nanoseconds (1_000_000_000);\n'
            Ada_SOP_Body[core][partition] += '\tprocedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is\n\t\tpragma Unreferenced (ARGUMENT);\n'
            Ada_SOP_Body[core][partition] += '\tbegin\n\t\tdelay ' + str ((max(hyperperiods['c1']['LOW'], hyperperiods['c1']['HIGH'], hyperperiods['c2']['LOW'], hyperperiods['c2']['HIGH']) / 1000000) + 2.0) + ';\n\t\tloop\n\t\t\tnull;\n\t\t\tAda.Text_IO.Put_Line ("end?");\n\t\tend loop;\n\tend LAST;\n\nend Set_Of_Procedures;'

            for task in tasks_on_current_partition_XML.findall('task'):
                t_id = int (str (task.find('ID').text))

                if len (str (t_id)) == 1:
                    t_id_RTEMS_classic_api_format = '0' + str(t_id)
                else:
                    t_id_RTEMS_classic_api_format = str(t_id)
            
                Ada_Units[core][partition] += '\t\tRTEMS.TASKS.CREATE(\n'
                Ada_Units[core][partition] += '\t\t\tRTEMS.BUILD_NAME(\'T\', \'_\', \'' + t_id_RTEMS_classic_api_format[0] + '\', \'' + t_id_RTEMS_classic_api_format[1] + '\'),\n'
                Ada_Units[core][partition] += '\t\t\t' + str (144 - int (task.find('priority').text)) + ',\n\t\t\tRTEMS.MINIMUM_STACK_SIZE,\n\t\t\tRTEMS.PREEMPT,\n\t\t\tRTEMS.DEFAULT_ATTRIBUTES,\n\t\t\tID_T_' + str(t_id) + ',\n\t\t\tSTATUS_T_' + str (t_id) + '\n\t\t);\n\n'                

            Ada_Units[core][partition] += '\n\t\t--  Start the tasks\n\n'

            for task in tasks_on_current_partition_XML.findall('task'):
                t_id = int (str (task.find('ID').text))
                Ada_Units[core][partition] += '\t\tRTEMS.TASKS.START(\n'
                Ada_Units[core][partition] += '\t\t\tID_T_' + str (t_id) + ',\n\t\t\tSet_Of_Procedures.T_' + str (t_id) + '_Body\'ACCESS,\n\t\t\t0,\n\t\t\tSTATUS_T_' + str (t_id) + '\n\t\t);\n\n'

            Ada_Units[core][partition] += '\t\tdelay To_Duration (Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod));\n\n'
            Ada_Units[core][partition] += '\t\t--  RTEMS.CPU_Usage.RESET;\n\n'
            Ada_Units[core][partition] += '\n\t\tAda.Text_IO.Put_Line ("");\n\n'
            Ada_Units[core][partition] += '\t\tif Single_Execution_Data.Partition_Id = "C1LOW" then\n\t\t\tAda.Text_IO.Put_Line ("New Execution");\n\t\t\tAda.Text_IO.Put_Line (Single_Execution_Data.System_Id);\n\t\tend if;\n'
            Ada_Units[core][partition] += '\t\tif Single_Execution_Data.Partition_Id = "C1HIGH" then\n\t\t\tdelay 2.0;\n\t\tend if;\n'
            Ada_Units[core][partition] += '\t\tif Single_Execution_Data.Partition_Id = "C2LOW" then\n\t\t\tdelay 4.0;\n\t\tend if;\n'
            Ada_Units[core][partition] += '\t\tif Single_Execution_Data.Partition_Id = "C2HIGH" then\n\t\t\tdelay 6.0;\n\t\tend if;\n'
            Ada_Units[core][partition] += '\n\t\tAda.Text_IO.Put_Line (Single_Execution_Data.Partition_Id);\n'
            Ada_Units[core][partition] += '\n\t\tAda.Text_IO.Put_Line ("Partition_Size: " & Single_Execution_Data.Partition_Size);\n\t\tAda.Text_IO.Put_Line ("Criticality Factor: " & Single_Execution_Data.Criticality_Factor);\n\t\tAda.Text_IO.Put_Line ("HI_Crit_Proportion: " & Single_Execution_Data.HI_Crit_Proportion);\n\t\tAda.Text_IO.Put_Line ("Partition_Utilization: " & Single_Execution_Data.Partition_Utilization);\n\t\tAda.Text_IO.Put_Line ("Is Valid: " & Boolean\'Image (Set_Of_Procedures.Is_Valid));'
            Ada_Units[core][partition] += '\n\t\tAda.Text_IO.Put_Line ("");\n\n\t\t--  rtems_cpu_usage_report\n\t\tRTEMS.CPU_Usage.Report;\n\n\t\tloop\n\t\t\tnull;\n\t\tend loop;\n\tend Init;\nend Periodic_Tasks;'
        
            f = open(Apps_Dir[core][partition] + 'periodic_tasks.adb', 'w')
            f.write(Ada_Units[core][partition])
            f.close()

            f = open(Apps_Dir[core][partition] + 'set_of_procedures.ads', 'w')
            f.write(Ada_SOP_Specs[core][partition])
            f.close()

            f = open(Apps_Dir[core][partition] + 'set_of_procedures.adb', 'w')
            f.write(Ada_SOP_Body[core][partition])
            f.close()

            shutil.copyfile (common_folder + 'initial_delay.ads', Apps_Dir[core][partition] + 'initial_delay.ads')
            shutil.copyfile (common_folder + 'production_workload.ads', Apps_Dir[core][partition] + 'production_workload.ads')
            shutil.copyfile (common_folder + 'production_workload.adb', Apps_Dir[core][partition] + 'production_workload.adb')
            shutil.copyfile (common_folder + 'production_workload.ads', Apps_Dir[core][partition] + 'production_workload.ads')
            shutil.copyfile (common_folder + 'periodic_tasks.ads', Apps_Dir[core][partition] + 'periodic_tasks.ads')
            shutil.copyfile (common_folder + 'workload_manager.ads', Apps_Dir[core][partition] + 'workload_manager.ads')
            shutil.copyfile (common_folder + 'config.h', Apps_Dir[core][partition] + 'config.h')
            shutil.copyfile (common_folder + 'Makefile_partition_' + core + partition, Apps_Dir[core][partition] + 'Makefile')
            shutil.copyfile (common_folder + 'Makefile_partition.am', Apps_Dir[core][partition] + 'Makefile.am')
            shutil.copyfile (common_folder + 'Makefile_partition.in', Apps_Dir[core][partition] + 'Makefile.in')
            shutil.copyfile (common_folder + 'rtems_init.c', Srcs_Dir[core][partition] + 'rtems_init.c')

            utils.edit_partition_makefile (Apps_Dir[core][partition] + 'Makefile', 'PROGRAM=' + Main_Units[core][partition])

        # Single_Execution_Data unit generation.
        # This unit contains specifics data for the current tasksets.
        # E.g. Tasksets hyperperiod
        for core in Single_Execution_Data:
          for partition in Single_Execution_Data[core]:
            hyperperiods[core][partition] = int(utils.compute_hyperperiod(periods[core][partition]))
            hyperperiods[core][partition] = int(utils.compute_hyperperiod(periods[core][partition]))        
        
        for core in Single_Execution_Data:
          current_core_XML = system.find ("core/[@id='" + core + "']")

          for partition in Single_Execution_Data[core]:
            current_partition_XML = current_core_XML.find ("partition/[@level='" + partition + "']")

            Single_Execution_Data[core][partition] = 'with System.Multiprocessors;\nuse System.Multiprocessors;\n\n' 
            Single_Execution_Data[core][partition] += 'package Single_Execution_Data is\n\tpragma Preelaborate;\n\n\tNumb_Of_Partitions : Positive := 4;\n\n'
            Single_Execution_Data[core][partition] += '\tExperiment_Hyperperiods : array (1 .. Numb_Of_Partitions) of Natural := (1 => ' + str(hyperperiods['c1']['LOW']) + ', 2 => ' + str(hyperperiods['c1']['HIGH']) + ', 3 => ' + str(hyperperiods['c2']['LOW']) + ', 4 => ' + str(hyperperiods['c2']['HIGH']) + ');\n\n'

            Single_Execution_Data[core][partition] += '\tId_Experiment : Integer := ' + str(experiment_id) + ';\n\tApproach : String := "' + approach.upper() + '";\n\tSystem_Id : String := "' + system_id + '";\n\tPartition_Id : String := "' + (core + partition).upper() + '";\n\n'
            # Single_Execution_Data[core][partition] += '\tId_Execution : String := "' + taskset_name + '";\n\n'

            Single_Execution_Data[core][partition] += '\t--  Needed to plot diagrams. These data are stored as strings in order to avoid issue related\n'
            Single_Execution_Data[core][partition] += '\t--  to differents types representations in differents languages (Python and Ada).\n'
            partition_size = str(current_partition_XML.find('partitionsize').text)
            partition_utilization = format (float (str(current_partition_XML.find('partitionutil').text)), '.3f')
            criticality_factor = str(system.find('criticalityfactor').text)
            hi_crit_proportion = str(system.find('perc').text)
            
            Single_Execution_Data[core][partition] += '\tPartition_Size : String := "' + partition_size + '";\n\tPartition_Utilization : String := "' + partition_utilization + '";\n\tCriticality_Factor : String := "' + criticality_factor + '";\n\tHI_Crit_Proportion : String := "' + hi_crit_proportion + '";\n\n'
            Single_Execution_Data[core][partition] += 'end Single_Execution_Data;'         

            f = open (Apps_Dir[core][partition] + 'single_execution_data.ads', 'w')
            f.write (Single_Execution_Data[core][partition])
            f.close()   

            # Generate Workload_Manager's body for current partition
            tasks_XML = current_partition_XML.find ('tasks')

            # Workload_Manager body generation
            workload_manager_unit = 'package body Workload_Manager is\n\n\ttype Workloads is array (Natural range <>) of Positive;\n\ttype Workloads_Access is access all Workloads;\n\n'

            overall_workloads_ada_array = '\n\tOverall_Workloads : constant array (1 .. ' + str(system.find('systemsize').text) + ') of Workloads_Access := (\n'

            get_workload_ada_function = '\t--  Get task "ID" \'s workload for its I-th job release.\n'
            get_workload_ada_function += '\tfunction Get_Workload(ID : Natural; I : Natural) return Positive is\n'
            get_workload_ada_function += '\tbegin\n\t\tif I in Overall_Workloads (ID)\'Range then\n\t\t\treturn Overall_Workloads (ID)(I);\n\t\telse\n\t\t\treturn Overall_Workloads (ID)(0);\n\t\tend if;\n\tend Get_Workload;\n\n'

            workloads_ada_array = {'naming': [], 'value': []}
            
            task_printed = 0

            workload_manager_unit += '\tWorkloads_Padding : aliased Workloads := (1, 1);\n'
            
            for task_XML in tasks_XML.findall('task'):
                task_index = int(task_XML.find('ID').text)
                workload_manager_unit += '\tWorkloads_T' + str(task_index) + ' : aliased Workloads := ('

                number_of_JR = int(hyperperiods[core][partition] // utils.to_microseconds_for_Ada (task_XML.find('period').text))
                values_for_job_release = []
                # Workloads computation for each job release for current task.
                workload = utils.microseconds_to_kilowhetstone_for_Ada_On_RTEMS_On_XM ( utils.to_microseconds_for_Ada (float(task_XML.find('executiontime').text)))

                for i in range (0, number_of_JR-1):
                    values_for_job_release.append (int((workload * random.uniform(config.TASK_MIN_REAL_UTILIZATION, config.TASK_MAX_REAL_UTILIZATION))) + 1)

                for i in range(0, len(values_for_job_release)):
                    if ((i+1) % 300) == 0: # start a new line in order to avoid compilation issues.
                        workload_manager_unit += '\n\t\t\t\t'
                    if i < len(values_for_job_release)-1:
                        workload_manager_unit += str(values_for_job_release[i]) + ', '
                    else:
                        workload_manager_unit += str(values_for_job_release[i]) + ', 1);\n'
                
                if len(values_for_job_release) == 0:
                    workload_manager_unit += '1, 1);\n'
                
                overall_workloads_ada_array += '\t\t' + str(task_index) + ' => Workloads_T' + str(task_index) + '\'Access'
                if task_printed != (int(current_partition_XML.find('partitionsize').text) - 1):
                    overall_workloads_ada_array += ',\n'
                else:
                    overall_workloads_ada_array += ',\n\t\tothers => Workloads_Padding\'Access\n\t);\n\n'
                task_printed += 1

            # Workload_Manager file unit generation
            workload_manager_unit += overall_workloads_ada_array + get_workload_ada_function + 'end Workload_Manager;'

            f = open(Apps_Dir[core][partition] + 'workload_manager.adb', 'w')
            f.write(workload_manager_unit)
            f.close()

        shutil.copyfile (common_folder + 'cora_ps7_init.tcl', system_dir + 'cora_ps7_init.tcl')
        shutil.copyfile (common_folder + 'cora_xsdb.ini', system_dir + 'cora_xsdb.ini')
        shutil.copyfile (common_folder + 'makefile_schema_2', system_dir + 'makefile')
        shutil.copyfile (common_folder + 'rules.mk', system_dir + 'rules.mk')
        shutil.copyfile (common_folder + 'xm_cf_schema_3.arm.xml', system_dir + 'xm_cf.arm.xml')

        tree_xm_cf = ET.parse(system_dir + 'xm_cf.arm.xml')
        root_xm_cf = tree_xm_cf.getroot()
        system_xml = root_xm_cf.find('HwDescription')
        processor_table_xml = system_xml.find('ProcessorTable')
        
        # XML XM Scheduling plan
        slot_id = 0
        for processor_xml in processor_table_xml.findall('Processor'):
          cyclic_plan_xml = processor_xml.find('CyclicPlanTable')
          plan_xml = cyclic_plan_xml.find('Plan')
          if processor_xml.attrib['id'] == str(0): # core 1
            plan_xml.attrib['majorFrame'] = str (major_frames['c1']) + "ms"
            for slot in IWRR_lists['c1']:
                current_slot_xml = ET.SubElement (plan_xml, 'Slot')
                current_slot_xml.attrib['id'] = str (slot_id)
                current_slot_xml.attrib['start'] = str (slot_duration['c1'] * slot_id) + 'ms'
                current_slot_xml.attrib['duration'] = str (slot_duration['c1']) + 'ms'
                current_slot_xml.attrib['partitionId'] = str (0) if slot == 'LOW' else str (1)
                slot_id += 1

          else: # core 2
            plan_xml.attrib['majorFrame'] = str (major_frames['c2']) + "ms"
            for slot in IWRR_lists['c2']:
                current_slot_xml = ET.SubElement (plan_xml, 'Slot')
                current_slot_xml.attrib['id'] = str (slot_id)
                current_slot_xml.attrib['start'] = str (slot_duration['c2'] * (slot_id - len (IWRR_lists['c1']))) + 'ms'
                current_slot_xml.attrib['duration'] = str (slot_duration['c2']) + 'ms'
                current_slot_xml.attrib['partitionId'] = str (2) if slot == 'LOW' else str (3)
                slot_id += 1

        # xmlns="http://www.xtratum.org/xm-arm-2.x" version="1.0.0" name="hello_world"
        root_xm_cf.attrib['xmlns'] = "http://www.xtratum.org/xm-arm-2.x"
        root_xm_cf.attrib['version'] = "1.0.0"
        root_xm_cf.attrib['name'] = system_id
        # print (system_dir + 'xm_cf.arm.xml')
        tree_xm_cf.write (system_dir + 'xm_cf.arm.xml')
        f = open(system_dir + 'cora_xsdb.ini', 'a')
        f.write('\n\nafter ' + str(int(max(hyperperiods['c1']['LOW'], hyperperiods['c1']['HIGH'], hyperperiods['c2']['LOW'], hyperperiods['c2']['HIGH']) /1000) + 8000))
        f.close()

        beautify_XML_XM_Files (experiment_id, system_id)

        # print ("\n----------------\n")

def beautify_XML_XM_Files(experiment_id, system_id):
    with open(config.Ada_RTEMS_XM_Paths[experiment_id]['MAST_IWRR'] + system_id + '/xm_cf.arm.xml', "r") as xmldata:
        parsing = xml.dom.minidom.parseString(xmldata.read())  # or xml.dom.minidom.parseString(xml_string)
        xml_pretty_str = parsing.toprettyxml()
        xmldata.close()

    with open(config.Ada_RTEMS_XM_Paths[experiment_id]['MAST_IWRR'] + system_id + '/xm_cf.arm.xml', "w") as xmldata:
      xmldata.write(xml_pretty_str)
      xmldata.close()