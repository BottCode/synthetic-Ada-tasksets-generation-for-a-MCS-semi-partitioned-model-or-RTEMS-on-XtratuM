import config
import os
import shutil
import math

import xml.etree.ElementTree as ET
import xml.dom.minidom

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

    is_schedulable, scheduling_plan = mast_analysis (system, experiment_id)
    
    if is_schedulable:
        save_as_XML (system, scheduling_plan, experiment_id, system_util, system_size, criticality_factor, hi_crit_proportion)
    
    return is_schedulable

##############
# compute_scheduling_plan
##############
def compute_scheduling_plan (system, experiment_id, system_path):
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

        for partition in system[core]:
            system_plan[core][partition]['W'] = math.ceil (system_plan[core][partition]['S'] / system_plan[core]['slot_size'])

    # Populate IWRR list, i.e. the effective scheduling plan.
    # Convention: the first partition to be scheduled is the HIGH-critical one.
    # print("\n", system_plan)
    for core in system_plan:
        W_LOW = system_plan[core]['LOW']['W']
        W_HIGH = system_plan[core]['HIGH']['W']
        while W_LOW > 0 or W_HIGH > 0:
            if W_HIGH > 0:
                system_plan[core]['IWRR_list'].append ('HIGH')
                W_HIGH = W_HIGH - 1
            if W_LOW > 0:
                system_plan[core]['IWRR_list'].append ('LOW')
                W_LOW = W_LOW - 1
        assert len (system_plan[core]['IWRR_list']) == (system_plan[core]['LOW']['W'] + system_plan[core]['HIGH']['W']), "AssertionError on system_plan[core]['IWRR_list']"

    return system_plan

##############
# mast_analysis
##############
def mast_analysis (system, experiment_id):

    #####
    # create MAST txt files and the overall system directory
    #####

    system_path = to_mast_file  (system, experiment_id)

    #####
    # generate partitions' scheduling plans according to the Interleaved WRR
    # and the following strategy: <https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/13#note_594713546> 
    #####

    scheduling_plan = compute_scheduling_plan (system, experiment_id, system_path)

    #####
    # analyze the overall system, i.e. check the schedulability
    # of both partitions on both core
    #####

    is_schedulable = analyze_system (system_path, experiment_id)
    
    if is_schedulable:
        return True, scheduling_plan
    return False, None

##############
# analyze_system
##############
def analyze_system (system_path, experiment_id):

    base_command_to_execute = "mast_analysis offset_based " + system_path

    for partition_file in os.listdir(system_path):
        partition_id = os.path.splitext(partition_file)[0]
        # os.system ("ls " + system_path + " > " + system_path + "/result_" + partition_id + ".txt")
        os.system (base_command_to_execute + "/" + partition_file + " > " + system_path + "/result_" + partition_id + ".txt")

        with open (system_path + "/result_" + partition_id + ".txt", "r") as result_file:
            if "NOT-SCHEDULABLE" in result_file.read():
                shutil.rmtree(system_path)
                return False
    
    shutil.rmtree(system_path)
    return True

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

    print("\n", scheduling_plan, "\n")
    print("\n", system, "\n\n")

    for core in system:
        current_core_XML = ET.SubElement (system_selector_XML, 'core', {'id': core})
        scheduling_plan_XML = ET.SubElement (current_core_XML, 'plan', {'majorFrame': str (scheduling_plan[core]['slot_size'])})
        
        for partition in system[core]:
            current_partition_XML = ET.SubElement (current_core_XML, 'partition', {'level': partition})
            
            weight_XML = ET.SubElement (current_partition_XML, 'weight')
            weight_XML.text = str (scheduling_plan[core][partition]['W'])
            
            partition_util_XML = ET.SubElement (current_partition_XML, 'partitionutil')
            partition_util_XML.text = str (scheduling_plan[core][partition]['U'])

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