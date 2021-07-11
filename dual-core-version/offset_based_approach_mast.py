import config
import os
import shutil

##############
# verify_schedulability
##############

def verify_schedulability (taskset, experiment_id):
    
    high_crit_tasks   = []
    low_crit_tasks  = []

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


    return mast_analysis (system, experiment_id)

##############
# mast_analysis
##############
def mast_analysis (system, experiment_id):

    #####
    # create MAST txt files and the overall system directory
    #####

    system_path = to_mast_file  (system, experiment_id)

    #####
    # analyze the overall system, i.e. check the schedulability
    # of both partitions on both core
    #####

    return analyze_system (system_path, experiment_id)

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
            lines = result_file.read().splitlines()
            last_line = lines[-1]
            if last_line == "Final analysis status: DONE":
                continue
            elif last_line == "Final analysis status: NOT-SCHEDULABLE":
                shutil.rmtree(system_path)
                return False
            else:
                print ("!!\n\nUnhandled MAST result: " + last_line + "\n\n!!")
                shutil.rmtree(system_path)
                os._exit ()
    
    shutil.rmtree(system_path)
    return True
    # os._exit(os.EX_OK)

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

                #print (MAST_text, "\n")

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
