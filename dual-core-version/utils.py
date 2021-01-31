import copy
import config

import os

import xml.etree.ElementTree as ET
import xml.dom.minidom

from shutil import copyfile, rmtree
import random

from math import gcd

def print_hyperperiod (hyperperiod):
  microseconds = hyperperiod
  seconds = microseconds / 1000000
  minutes = seconds / 60
  hours = minutes / 60
  print ("microseconds => ", microseconds, ", seconds => ", seconds, ", minutes => ", minutes, ", hours => ", hours)

def compute_hyperperiod (periods):
  # print("p:", periods)
  lcm = periods[0]
  for i in periods[1:]:
    lcm = lcm*i//gcd(lcm, i)
  # print(lcm)
  return lcm

# cast a period from string to an integer (microseconds).
# check XML to see how <CHI> and <CLO> are represented.
# From that shape, we need microseconds.
def to_microseconds_for_Ada (period):
  multiplier = 1000
  final_number = int (float(period) * multiplier)
  #print(final_number)
  #i = len(final_number) - 1
  #for c in reversed (final_number):
  #  print(c)
  return final_number

def microseconds_to_kilowhetstone_for_Ada_On_RTEMS_On_XM (microseconds):
  multiplier = 0
  divider = 0
  # According to some evaluations:
  #  - 3 KW    => 100 microseconds
  #  - 36 KW   => 1000 microseconds
  #  - 366 KW  => 10000 microseconds
  #  - 3667 KW => 100000 microseconds 

  if microseconds < 1000:
    multiplier = 3
    divider = 100
  elif microseconds < 10000:
    multiplier = 36
    divider = 1000
  elif microseconds < 100000:
    multiplier = 366
    divider = 10000
  else:
    multiplier = 3667
    divider = 100000
  
  result = int( (microseconds/divider) * multiplier)
  if result == 0:
    result = 1
  return result

def microseconds_to_kilowhetstone_for_ravenscar_runtime (microseconds):
  multiplier = 0
  divider = 0
  # According to some evaluations:
  #  - 13 KW    => 100 microseconds          +/- 1.75  microseconds
  #  - 132 KW   => 1000 microseconds         +/- 1.8  microseconds
  #  - 1325 KW  => 10000 microseconds        +/- 1.8  microseconds
  #  - 13258 KW => 100000 microseconds +/- 1.875 microseconds

  if microseconds < 1000:
    multiplier = 13
    divider = 100
  elif microseconds < 10000:
    multiplier = 132
    divider = 1000
  elif microseconds < 100000:
    multiplier = 1325
    divider = 10000
  else:
    multiplier = 13258
    divider = 100000
  
  result = int( (microseconds/divider) * multiplier)
  if result == 0:
    result = 1
  return result
  


def CLEAN_ALL():
  for i in range(4):
    clean_XML_and_Ada_Files(i+1)

def clean_XML_and_Ada_Files(experiment_id):
  xml_template = './XML_tasksets/template.xml'

  for path in config.XML_Files[experiment_id]:
    copyfile(xml_template, config.XML_Files[experiment_id][path])

  for path in config.Ada_Paths[experiment_id]:
    for dirname in os.listdir(config.Ada_Paths[experiment_id][path]):
      dirpath = os.path.join(config.Ada_Paths[experiment_id][path], dirname)
      if os.path.exists(dirpath) and dirname != '.gitkeep':
        rmtree(dirpath) 

  for path in config.Ada_No_Mig_Paths[experiment_id]:
    for dirname in os.listdir(config.Ada_No_Mig_Paths[experiment_id][path]):
      dirpath = os.path.join(config.Ada_No_Mig_Paths[experiment_id][path], dirname)
      if os.path.exists(dirpath) and dirname != '.gitkeep':
        rmtree(dirpath)

  for path in config.Ada_RTEMS_XM_Paths[experiment_id]:
    for dirname in os.listdir(config.Ada_RTEMS_XM_Paths[experiment_id][path]):
      dirpath = os.path.join(config.Ada_RTEMS_XM_Paths[experiment_id][path], dirname)
      if os.path.exists(dirpath) and dirname != '.gitkeep':
        rmtree(dirpath)

def edit_partition_makefile (file_name, line):
  """ Insert given string as a new line at the beginning of a file """
  # define name of temporary dummy file
  dummy_file = file_name + '.bak'
  # open original file in read mode and dummy file in write mode
  with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
    # Write given line to the dummy file
    write_obj.write(line + '\n')
    # Read lines from original file one by one and append them to the dummy file
    for line in read_obj:
      write_obj.write(line)

  # remove original file
  os.remove(file_name)
  # Rename dummy file as the original file
  os.rename(dummy_file, file_name)

# generate two XtratuM partitions, each of them concerning an Ada application on top of RTEMS (XM -> RTEMS -> Ada app)
def save_taskset_as_Ada_On_RTEMS_On_XM (experiment_id):
  common_folder = config.Ada_RTEMS_Common_Folder

  for approach in config.XML_Files[experiment_id]:
    tree = ET.parse(config.XML_Files[experiment_id][approach])
    root = tree.getroot()

    for taskset in root.findall('taskset'):
      periods = {'p1': [], 'p2': []} # needed for hyperperiod computations
      hyperperiods = {'p1': 0, 'p2': 0} # needed for hyperperiod computations

      taskset_id = int(taskset.find('tasksetid').text)
      if taskset_id != -1:
        taskset_name = taskset.find('executionid').text

        Ada_Units = {'p1': '', 'p2': ''}
        Ada_Units_Files_Name = {'p1': 'taskset_' + taskset_name + '_p1.ads', 'p2': 'taskset_' + taskset_name + '_p2.ads'}
        # Ada Set Of Procedures
        Ada_SOP_Specs = {'p1': '', 'p2': ''}
        Ada_SOP_Body = {'p1': '', 'p2': ''}
        Single_Execution_Data = {'p1': '', 'p2': ''}
        Main_Units = {'p1': '', 'p2': ''}
        Mains_Files_Name = {'p1': '', 'p2': ''}
        Tasksets_Name = {'p1': str(taskset.find('executionid').text) + '_' + 'p1', 'p2': str(taskset.find('executionid').text) + '_' + 'p2'}

        # dir containing both partitions
        taskset_dir = config.Ada_RTEMS_XM_Paths[experiment_id][approach] + taskset_name + '/'
        os.mkdir(taskset_dir)

        # dir containing src code
        Srcs_Dir = {'p1': taskset_dir + 'p0/', 'p2': taskset_dir + 'p1/'}
        Apps_Dir = {'p1': Srcs_Dir['p1'] + 'app/', 'p2': Srcs_Dir['p2'] + 'app/'}
        
        os.mkdir(Srcs_Dir['p1'])
        os.mkdir(Srcs_Dir['p2'])
        os.mkdir(Apps_Dir['p1'])
        os.mkdir(Apps_Dir['p2'])

        # Mains generation, one for each partition 
        for p in Main_Units:
          Main_Units[p] = 'main_' + Tasksets_Name[p]
          Mains_Files_Name[p] = Main_Units[p] + '.adb'
          main = 'with System;\nwith Periodic_Tasks;\n\n'
          main += 'procedure ' + Main_Units[p] + ' is\n'
          main += "\tpragma Priority (114);\n"
          main += 'begin\n\tPeriodic_Tasks.Init;\nend ' + Main_Units[p] + ';'

          # create main unit Ada file
          f = open(Apps_Dir[p] + Mains_Files_Name[p], 'w')
          f.write(main)
          f.close()

          Ada_Units[p] = 'with Ada.Real_Time; use Ada.Real_Time;\n\nwith Ada.Text_IO;\n\nwith System.Multiprocessors;\nuse System.Multiprocessors;\n\n'
          Ada_Units[p] += 'with Single_Execution_Data;\nwith Production_Workload;\nwith Set_Of_Procedures;\nwith Workload_Manager;\nwith Initial_Delay;\n\nwith RTEMS;\nwith RTEMS.TASKS;\nwith RTEMS.CPU_Usage;\n\n'
          # Ada_Units[p] += 'use Periodic_Tasks;\n\npackage taskset_' + Tasksets_Name[p] + ' is\n\n'
          Ada_Units[p] += 'package body Periodic_Tasks is\n\n'
          Ada_Units[p] += '\tfunction Get_Longest_Hyperperiod return Natural is\n\tbegin\n'
          Ada_Units[p] += '\t\tif Single_Execution_Data.Experiment_Hyperperiods (1) > Single_Execution_Data.Experiment_Hyperperiods (2) then\n'
          Ada_Units[p] += '\t\t\treturn Single_Execution_Data.Experiment_Hyperperiods (1);\n\t\tend if;\n\n'
          Ada_Units[p] += '\t\treturn Single_Execution_Data.Experiment_Hyperperiods (2);\n\t end Get_Longest_Hyperperiod;\n\n'
          Ada_Units[p] += '\t------------\n\t--  Init  --\n\t------------\n\n'
          Ada_Units[p] += '\tprocedure Init is\n\t\tNext_Period : constant Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);\n\t\tPeriod_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod);\n\n'
          
          Ada_SOP_Specs[p] += 'with RTEMS.TASKS;\n\npackage Set_Of_Procedures is\n\n'
          Ada_SOP_Body[p] += 'with Ada.Real_Time; use Ada.Real_Time;\n\nwith Single_Execution_Data;\nwith Production_Workload;\nwith Workload_Manager;\nwith Initial_Delay;\n\nwith Ada.Text_IO;\n\n'
          Ada_SOP_Body[p] += 'package body Set_Of_Procedures is\n\n\tprocedure Work (Period : Duration; ID : Natural);\n\tpragma No_Return (Work);\n\n'
          Ada_SOP_Body[p] += '\tprocedure Work (Period : Duration; ID : Natural) is\n'
          Ada_SOP_Body[p] += '\t\t--  Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);\n\t\t--  Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Period);\n\t\tI : Natural := 0;\n'
          Ada_SOP_Body[p] += '\t\tFake_Status : RTEMS.STATUS_CODES;\n\t\tFake_Previous_Mode : RTEMS.MODE;\t\tDelayed_At : Ada.Real_Time.Time;\n\t\tWaked_At : Ada.Real_Time.Time;\n\t\tDeadline : Ada.Real_Time.Time;\n\t\tTime_To_Sleep : Duration := 0.0;\n\t\tNow : Ada.Real_Time.Time;\n'
          # Ada_SOP_Body[p] += '\tbegin\n\t\tloop\n\t\t\tdelay until Next_Period;\n\n\t\t\tProduction_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));\n\n\t\t\tI := I + 1;\n\n\t\t\tNext_Period := Next_Period + Period_To_Add;\n\t\tend loop;\n\tend Work;\n\n'
          Ada_SOP_Body[p] += '\tbegin\n\n\t\tdelay 2.0;\n\n\t\tloop\n\t\t\tDeadline := Ada.Real_Time.Clock + To_Time_Span (Period);\n\n\t\t\tProduction_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));\n\n\t\t\tI := I + 1;\n\n\t\t\tNow := Ada.Real_Time.Clock;\n\n\t\t\tif Now <= Deadline then\n\n\t\t\t\tRTEMS.TASKS.MODE (RTEMS.NO_PREEMPT, 0, Fake_Previous_Mode, Fake_Status);\n\n\t\t\t\tTime_To_Sleep := To_Duration (Deadline - Ada.Real_Time.Clock);\n\t\t\t\t--  Delayed_At := Ada.Real_Time.Clock;\n\t\t\t\tdelay Time_To_Sleep;\n\t\t\t\t--  Waked_At := Ada.Real_Time.Clock;\n\n\t\t\t\tRTEMS.TASKS.MODE (RTEMS.PREEMPT, 0, Fake_Previous_Mode, Fake_Status);\n\t\t\t\t--  Ada.Text_IO.Put_Line ("Error Task " & Natural\'Image (ID) & ": " & Duration\'Image (Abs (Time_To_Sleep - (To_Duration (Waked_At - Delayed_At))) * 1_000) & " milliseconds");\n'
          Ada_SOP_Body[p] += '\n\t\t\telse\n\t\t\t\tAda.Text_IO.Put_Line ("DM Task " & Natural\'Image (ID));\n\t\t\tend if;\n\t\tend loop;\n\tend Work;\n\n'

          current_partition_XML = taskset.find ('core1') if p == 'p1' else taskset.find ('core2')
          tasks_on_current_partition_XML = current_partition_XML.find('tasks')

          for t in tasks_on_current_partition_XML.findall('task'):
            Ada_Units[p] += '\t\tID_T_' + str(t.find('ID').text) + ' : RTEMS.ID;\n'
            Ada_Units[p] += '\t\tSTATUS_T_' + str(t.find('ID').text) + ' : RTEMS.STATUS_CODES;\n'

            Ada_SOP_Specs[p] += '\tprocedure T_' + str(t.find('ID').text) + '_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);\n'
            Ada_SOP_Specs[p] += '\tpragma Convention (C, T_' + str(t.find('ID').text) + '_Body);\n\n'

            Ada_SOP_Body[p] += '\tprocedure T_' + str(t.find('ID').text) + '_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is\n\t\tpragma Unreferenced (ARGUMENT);\n\t\tPeriod : Duration := ' + str((to_microseconds_for_Ada (t.find('period').text)) / 1000000) + ';\n'
            Ada_SOP_Body[p] += '\t\tID : Natural := ' + str(t.find('ID').text) + ';\n'
            Ada_SOP_Body[p] += '\tbegin\n\t\tWork (Period, ID);\n\tend T_' + str(t.find('ID').text) + '_Body;\n\n'

            periods[p].append (int(to_microseconds_for_Ada (t.find('period').text)))

          Ada_Units[p] += '\n\t\tID_T_LAST : RTEMS.ID;\n\t\tSTATUS_T_LAST : RTEMS.STATUS_CODES;\n\tbegin\n\n'
          Ada_SOP_Specs[p] += '\tprocedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT);\n'
          Ada_SOP_Specs[p] += '\tpragma Convention (C, LAST);\n\nend Set_Of_Procedures;'
          # Ada_SOP_Body[p] += '\tprocedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is\n\t\tpragma Unreferenced (ARGUMENT);\n\t\tNext_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Nanoseconds (1_000_000_000);\n'
          Ada_SOP_Body[p] += '\tprocedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is\n\t\tpragma Unreferenced (ARGUMENT);\n'
          Ada_SOP_Body[p] += '\tbegin\n\t\tdelay ' + str ((max(hyperperiods['p1'], hyperperiods['p2']) / 1000000) + 2.0) + ';\n\t\tloop\n\t\t\tnull;\n\t\t\tAda.Text_IO.Put_Line ("end?");\n\t\tend loop;\n\tend LAST;\n\nend Set_Of_Procedures;'

          for t in tasks_on_current_partition_XML.findall('task'):
            t_id = int(str(t.find('ID').text))

            if len(str(t_id)) == 1:
              t_id_RTEMS_classic_api_format = '0' + str(t_id)
            else:
              t_id_RTEMS_classic_api_format = str(t_id)
            
            Ada_Units[p] += '\t\tRTEMS.TASKS.CREATE(\n'
            Ada_Units[p] += '\t\t\tRTEMS.BUILD_NAME(\'T\', \'_\', \'' + t_id_RTEMS_classic_api_format[0] + '\', \'' + t_id_RTEMS_classic_api_format[1] + '\'),\n'
            Ada_Units[p] += '\t\t\t' + str(144 - int(t.find('priority').text)) + ',\n\t\t\tRTEMS.MINIMUM_STACK_SIZE,\n\t\t\tRTEMS.PREEMPT,\n\t\t\tRTEMS.DEFAULT_ATTRIBUTES,\n\t\t\tID_T_' + str(t_id) + ',\n\t\t\tSTATUS_T_' + str(t_id) + '\n\t\t);\n\n'

          # Ada_Units[p] += '\t\tRTEMS.TASKS.CREATE(\n\t\tRTEMS.BUILD_NAME(\'L\', \'A\', \'S\', \'T\'),\n\t\t\t255,\n\t\t\tRTEMS.MINIMUM_STACK_SIZE,\n\t\t\tRTEMS.PREEMPT,\n\t\t\tRTEMS.DEFAULT_ATTRIBUTES,\n\t\t\tID_T_LAST,\n\t\t\tSTATUS_T_LAST\n\t\t);\n'
          Ada_Units[p] += '\n\t\t--  Start the tasks\n\n'
          # Ada_Units[p] += '\t\tRTEMS.TASKS.START(\n\t\t\tID_T_LAST,\n\t\t\tSet_Of_Procedures.LAST\'ACCESS,\n\t\t\t0,\n\t\t\tSTATUS_T_LAST\n\t\t);\n\n'

          for t in tasks_on_current_partition_XML.findall('task'):
            t_id = int(str(t.find('ID').text))
            Ada_Units[p] += '\t\tRTEMS.TASKS.START(\n'
            Ada_Units[p] += '\t\t\tID_T_' + str(t_id) + ',\n\t\t\tSet_Of_Procedures.T_' + str(t_id) + '_Body\'ACCESS,\n\t\t\t0,\n\t\t\tSTATUS_T_' + str(t_id) + '\n\t\t);\n\n'

          Ada_Units[p] += '\t\tdelay To_Duration (Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod));\n\n'
          Ada_Units[p] += '\t\t--  RTEMS.CPU_Usage.RESET;\n\n'
          Ada_Units[p] += '\t\tif Single_Execution_Data.Partition_Id = "P2" then\n\t\t\tdelay 2.0;\n\t\t\tAda.Text_IO.Put_Line ("Second Partition");\n\t\tend if;\n'
          Ada_Units[p] += '\n\t\tAda.Text_IO.Put_Line ("");\n\n\t\tif Single_Execution_Data.Partition_Id = "P1" then\n\t\t\tAda.Text_IO.Put_Line ("New Execution");\n\t\t\tAda.Text_IO.Put_Line (Single_Execution_Data.Id_Execution);\n\t\t\tAda.Text_IO.Put_Line ("First Partition");\n\t\tend if;\n\n\t\tAda.Text_IO.Put_Line ("");\n\n\t\t--  rtems_cpu_usage_report\n\t\tRTEMS.CPU_Usage.Report;\n\n\t\tloop\n\t\t\tnull;\n\t\tend loop;\n\tend Init;\nend Periodic_Tasks;'

          tasks_XML = current_partition_XML.find ('tasks')

          f = open(Apps_Dir[p] + 'periodic_tasks.adb', 'w')
          f.write(Ada_Units[p])
          f.close()

          f = open(Apps_Dir[p] + 'set_of_procedures.ads', 'w')
          f.write(Ada_SOP_Specs[p])
          f.close()

          f = open(Apps_Dir[p] + 'set_of_procedures.adb', 'w')
          f.write(Ada_SOP_Body[p])
          f.close()
   
          copyfile (common_folder + 'initial_delay.ads', Apps_Dir[p] + 'initial_delay.ads')
          copyfile (common_folder + 'production_workload.ads', Apps_Dir[p] + 'production_workload.ads')
          copyfile (common_folder + 'production_workload.adb', Apps_Dir[p] + 'production_workload.adb')
          copyfile (common_folder + 'production_workload.ads', Apps_Dir[p] + 'production_workload.ads')
          copyfile (common_folder + 'periodic_tasks.ads', Apps_Dir[p] + 'periodic_tasks.ads')
          copyfile (common_folder + 'workload_manager.ads', Apps_Dir[p] + 'workload_manager.ads')
          copyfile (common_folder + 'config.h', Apps_Dir[p] + 'config.h')
          copyfile (common_folder + 'Makefile_partition_' + p, Apps_Dir[p] + 'Makefile')
          copyfile (common_folder + 'Makefile_partition.am', Apps_Dir[p] + 'Makefile.am')
          copyfile (common_folder + 'Makefile_partition.in', Apps_Dir[p] + 'Makefile.in')
          copyfile (common_folder + 'rtems_init.c', Srcs_Dir[p] + 'rtems_init.c')

          edit_partition_makefile (Apps_Dir[p] + 'Makefile', 'PROGRAM=' + Main_Units[p])
          

        # Single_Execution_Data unit generation.
        # This unit contains specifics data for the current tasksets.
        # E.g. Tasksets hyperperiod
        
        hyperperiods['p1'] = int(compute_hyperperiod(periods['p1']))
        hyperperiods['p2'] = int(compute_hyperperiod(periods['p2']))

        for p in Single_Execution_Data:
          Single_Execution_Data[p] = 'with System.Multiprocessors;\nuse System.Multiprocessors;\n\n' 
          Single_Execution_Data[p] += 'package Single_Execution_Data is\n\tpragma Preelaborate;\n\n\tNumb_Of_Partitions : Positive := 2;\n\n'
          Single_Execution_Data[p] += '\tExperiment_Hyperperiods : array (1 .. Numb_Of_Partitions) of Natural := (1 => ' + str(hyperperiods['p1']) + ', 2 => ' + str(hyperperiods['p1']) + ');\n\n'

          Single_Execution_Data[p] += '\tId_Experiment : Integer := ' + str(experiment_id) + ';\n\tApproach : String := "' + approach.upper() + '";\n\tTaskset_Id : Integer := ' + str(taskset_id) + ';\n\tPartition_Id : String := "' + p.upper() + '";\n\n'
          Single_Execution_Data[p] += '\tId_Execution : String := "' + taskset_name + '";\n\n'

          Single_Execution_Data[p] += '\t--  Needed to plot diagrams. These data are stored as strings in order to avoid issue related\n'
          Single_Execution_Data[p] += '\t--  to differents types representations in differents languages (Python and Ada).\n'
          taskset_size = str(taskset.find('tasksetsize').text)
          taskset_utilization = str(taskset.find('tasksetutilization').text)
          criticality_factor = str(taskset.find('criticalityfactor').text)
          hi_crit_proportion = str(taskset.find('perc').text)
          
          Single_Execution_Data[p] += '\tTaskset_Size : String := "' + taskset_size + '";\n\tTaskset_Utilization : String := "' + taskset_utilization + '";\n\tCriticality_Factor : String := "' + criticality_factor + '";\n\tHI_Crit_Proportion : String := "' + hi_crit_proportion + '";\n\n'
          Single_Execution_Data[p] += 'end Single_Execution_Data;'

          f = open(Apps_Dir[p] + 'single_execution_data.ads', 'w')
          f.write(Single_Execution_Data[p])
          f.close()

          # Generate Workload_Manager's body for current partition
          current_partition_XML = taskset.find ('core1') if p == 'p1' else taskset.find ('core2')
          tasks_XML = current_partition_XML.find ('tasks')

          # Workload_Manager body generation
          workload_manager_unit = 'package body Workload_Manager is\n\n\ttype Workloads is array (Natural range <>) of Positive;\n\ttype Workloads_Access is access all Workloads;\n\n'

          overall_workloads_ada_array = '\n\tOverall_Workloads : constant array (1 .. ' + str(taskset.find('tasksetsize').text) + ') of Workloads_Access := (\n'

          get_workload_ada_function = '\t--  Get task "ID" \'s workload for its I-th job release.\n'
          get_workload_ada_function += '\tfunction Get_Workload(ID : Natural; I : Natural) return Positive is\n'
          get_workload_ada_function += '\tbegin\n\t\tif I in Overall_Workloads (ID)\'Range then\n\t\t\treturn Overall_Workloads (ID)(I);\n\t\telse\n\t\t\treturn Overall_Workloads (ID)(0);\n\t\tend if;\n\tend Get_Workload;\n\n'

          workloads_ada_array = {'naming': [], 'value': []}
          
          task_printed = 0

          workload_manager_unit += '\tWorkloads_Padding : aliased Workloads := (1, 1);\n' 
          for task_XML in tasks_XML.findall('task'):
            task_index = int(task_XML.find('ID').text)

            workload_manager_unit += '\tWorkloads_T' + str(task_index) + ' : aliased Workloads := ('

            number_of_JR = int(hyperperiods[p] // to_microseconds_for_Ada (task_XML.find('period').text))
            values_for_job_release = []

            # Workloads computation for each job release for current task.
            workload = microseconds_to_kilowhetstone_for_Ada_On_RTEMS_On_XM ( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))
            if task_XML.find('migrating').text == 'False':
              for i in range (0, number_of_JR-1):
                values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
            else:
              for i in range (0, number_of_JR-1):
                values_for_job_release.append (int((workload * random.uniform(0.4, 0.5))) + 1)

            for i in range(0, len(values_for_job_release)):
              if ((i+1) % 300) == 0: # start a new line in order to avoid compilation issues.
                workload_manager_unit += '\n\t\t\t\t'
              if i < len(values_for_job_release)-1:
                workload_manager_unit += str(values_for_job_release[i]) + ', '
              else:
                workload_manager_unit += str(values_for_job_release[i]) + ');\n'
            
            overall_workloads_ada_array += '\t\t' + str(task_index) + ' => Workloads_T' + str(task_index) + '\'Access'
            if task_printed != (int(tasks_XML.find('total').text) - 1):
              overall_workloads_ada_array += ',\n'
            else:
              overall_workloads_ada_array += ',\n\t\tothers => Workloads_Padding\'Access\n\t);\n\n'
            task_printed += 1
          # Workload_Manager file unit generation
          workload_manager_unit += overall_workloads_ada_array + get_workload_ada_function + 'end Workload_Manager;'
          f = open(Apps_Dir[p] + 'workload_manager.adb', 'w')
          f.write(workload_manager_unit)
          f.close()

        copyfile (common_folder + 'cora_ps7_init.tcl', taskset_dir + 'cora_ps7_init.tcl')
        copyfile (common_folder + 'cora_xsdb.ini', taskset_dir + 'cora_xsdb.ini')
        copyfile (common_folder + 'makefile', taskset_dir + 'makefile')
        copyfile (common_folder + 'rules.mk', taskset_dir + 'rules.mk')
        copyfile (common_folder + 'xm_cf.arm.xml', taskset_dir + 'xm_cf.arm.xml')

        f = open(taskset_dir + 'cora_xsdb.ini', 'a')
        f.write('\n\nafter ' + str( int(max(hyperperiods['p1'], hyperperiods['p2']) /1000) + 4000))
        f.close()

          

# generate a GPR project compiling with Ravenscar supporting MCS runtime
def save_taskset_as_Ada (experiment_id):
  q = 0
  string_tasks = []

  for approach in config.XML_Files[experiment_id]:
    tree = ET.parse(config.XML_Files[experiment_id][approach])
    root = tree.getroot()

    for taskset in root.findall('taskset'):
      periods_c1 = [] # needed for hyperperiod computations
      periods_c2 = []

      taskset_id = int(taskset.find('tasksetid').text)
      if taskset_id != -1:
        Ada_Unit = ''
        Main_Unit = ''

        taskset_name = taskset.find('executionid').text

        # Main generation
        main_name = 'main_' + taskset_name
        main_file_name = main_name + '.adb'
        main_withed_units = 'with System;\nwith Periodic_Tasks;\n\nwith taskset_' + taskset_name + ';\n' 
        main_unreferenced_units = 'pragma Unreferenced (taskset_'  + taskset_name + ');\n\n'
        main_procedure = 'procedure ' + main_name + ' is\n'
        main_decl_section = "    pragma Priority (System.Priority'Last);\n    pragma CPU (1);\n"
        main_body = 'begin\n    Periodic_Tasks.Init;\nend ' + main_name + ';'
        
        Main_Unit += main_withed_units + main_unreferenced_units +  main_procedure + main_decl_section + main_body

        # .gpr file project generation
        project_file_name = taskset_name + '.gpr'
        project = 'project ' + taskset_name + ' is\n\n'
        project += '\tfor Languages use ("ada");\n\tfor Main use ("' + main_file_name + '");\n\tfor Source_Dirs use ("src", "../../../common");\n\tfor Object_Dir use "obj";\n    for Runtime ("ada") use '
        runtime_dir = config.RUNTIME_DIR + ';\n'
        project += runtime_dir + '\tfor Target use "arm-eabi";\n\n'
        project += '\tpackage Compiler is\n        for Switches ("ada") use ("-g", "-gnatwa", "-gnatQ");\n    end Compiler;\n\n'
        project += '\tpackage Builder is\n        for Switches ("ada") use ("-g", "-O0");\n    end Builder;\n\n'
        project += 'end ' + taskset_name + ';'

        # Makefile generation

        make_all = 'all:  test\n\n'
        make_test = 'test:\n\tgprbuild ' + project_file_name + '\n\n'
        make_clean = 'clean:\n\tgprclean ' + project_file_name + '\n\n'
        makefile = make_all + make_test + make_clean

        # Ada taskset unit generation

        withed_unit = 'with Periodic_Tasks;\nuse Periodic_Tasks;\n'
        package_name = '\npackage taskset_' + taskset_name + ' is\n\n'
        file_name = 'taskset_' + taskset_name + '.ads'

        Ada_Unit += withed_unit + package_name

        cores_XML = [taskset.find('core1'), taskset.find('core2')]

        task_printed = 0
        for core_XML in cores_XML:
          tasks_XML = core_XML.find('tasks')
          
          for task_XML in tasks_XML.findall('task'):
            current_task = '  T_'
            current_task += task_XML.find('ID').text + ' : '

            if task_XML.find('criticality').text == 'HIGH':
              current_task += 'High_Crit ('
              workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CHI').text)))
            else:
              current_task += 'Low_Crit ('
              workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))
            
            current_task += 'Id => ' + task_XML.find('ID').text + ', '

            if core_XML == taskset.find('core2'):
              current_task += 'Pri => ' + str(int(task_XML.find('priority').text)+q) + ', '
              current_task += 'Hosting_Migrating_Tasks_Priority => ' + str(int(task_XML.find('hostingmigpriority').text)+q) + ', '
            else:
              current_task += 'Pri => ' + task_XML.find('priority').text + ', '
              current_task += 'Hosting_Migrating_Tasks_Priority => ' + task_XML.find('hostingmigpriority').text + ', '

            if task_XML.find('criticality').text == 'LOW':
              if core_XML == taskset.find('core1'):
                current_task += 'On_Target_Core_Priority => ' + str(int(task_XML.find('targetpriority').text)+q) + ', '
              else:
                current_task += 'On_Target_Core_Priority => ' + task_XML.find('targetpriority').text + ', '
            
            current_task += 'Low_Critical_Budget => ' + str(to_microseconds_for_Ada (task_XML.find('CLO').text)) + ', '

            if task_XML.find('criticality').text == 'HIGH':
              current_task += 'High_Critical_Budget => ' + str(to_microseconds_for_Ada (task_XML.find('CHI').text)) + ', '
            else:
              current_task += 'Is_Migrable => ' + task_XML.find('migrating').text + ', '
            
            current_task += 'Workload => ' + str(workload) + ', ' # + task_XML.find('workload').text + ', '
            current_task += 'Period => ' + str(to_microseconds_for_Ada (task_XML.find('period').text)) + ', '
            current_task += 'Reduced_Deadline => ' + str(to_microseconds_for_Ada (task_XML.find('reduceddead').text)) + ', '

            if task_XML.find('criticality').text == 'HIGH':
              if (core_XML.tag == 'core1' and taskset.find('migonc2').text == 'TRUE') or (core_XML.tag == 'core2' and taskset.find('migonc1').text == 'TRUE'):
                current_task += 'Could_Exceed => True, '
              else:
                current_task += 'Could_Exceed => False, '

            current_task += 'CPU_Id => ' + ('1' if core_XML.tag == 'core1' else '2') + ');'

            if task_XML.find('migrating').text == "True":
              periods_c1.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))
              periods_c2.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))
            else:
              if core_XML == taskset.find('core1'):
                periods_c1.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))
              else:
                periods_c2.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))

            Ada_Unit += current_task + '\n'

            string_tasks.append(current_task)
            # print(current_task)

        Ada_Unit += '\nend taskset_' + taskset_name + ';\n'

        # Single_Execution_Data unit generation.
        # This unit contains specifics data for the current tasksets.
        # E.g. Tasksets hyperperiod
        
        hyperperiod_core_1 = int(compute_hyperperiod(periods_c1))
        hyperperiod_core_2 = int(compute_hyperperiod(periods_c2))
        taskset_size = str(taskset.find('tasksetsize').text)

        if experiment_id == 4 and int (taskset_size) >= 25:
          # Generate config.EXPERIMENTS_REPETITIONS differents workloads sets corresponding to config.EXPERIMENTS_REPETITIONS experiment executions
          for repetition_id in range(1, config.EXPERIMENTS_REPETITIONS + 1):
            task_printed = 0
            
            single_execution_data_unit = ''
            single_execution_data_withed_package = 'with System.Multiprocessors;\nuse System.Multiprocessors;\n\n' 
            single_execution_data_unit += single_execution_data_withed_package + 'package Single_Execution_Data is\n\tpragma Preelaborate;\n\n'
            single_execution_data_spec = '\tExperiment_Hyperperiods : array (CPU) of Natural := (CPU\'First => ' + str(hyperperiod_core_1) + ', CPU\'Last => ' + str(hyperperiod_core_2) + ');\n\n'
            # single_execution_data_spec = '\tExperiment_Hyperperiod_CPU_1 : Natural := ' + str(hyperperiod_core_1) + ';\n\n\tExperiment_Hyperperiod_CPU_2 : Natural := ' + str(hyperperiod_core_2) + ';\n\n'

            single_execution_data_spec += '\tId_Experiment : Integer := ' + str(experiment_id) + ';\n\tApproach : String := "' + approach.upper() + '";\n\tTaskset_Id : Integer := ' + str(taskset_id) + ';\n\n'

            single_execution_data_spec += '\tId_Execution : String := "' + taskset_name + '_v' + str(repetition_id) + '";\n\n'

            data_for_plotting = '\t--  Needed to plot diagrams. These data are stored as strings in order to avoid issue related\n'
            data_for_plotting += '\t--  to differents types representations in differents languages (Python and Ada).\n'
            
            taskset_utilization = str(taskset.find('tasksetutilization').text)
            criticality_factor = str(taskset.find('criticalityfactor').text)
            hi_crit_proportion = str(taskset.find('perc').text)
            
            data_for_plotting += '\tTaskset_Size : String := "' + taskset_size + '";\n\tTaskset_Utilization : String := "' + taskset_utilization + '";\n\tCriticality_Factor : String := "' + criticality_factor + '";\n\tHI_Crit_Proportion : String := "' + hi_crit_proportion + '";\n\n'

            single_execution_data_spec += data_for_plotting
            single_execution_data_unit += single_execution_data_spec + 'end Single_Execution_Data;'

            # Workload_Manager body generation
            workload_manager_unit = 'package body Workload_Manager is\n\n\ttype Workloads is array (Natural range <>) of Positive;\n\ttype Workloads_Access is access all Workloads;\n\n'

            overall_workloads_ada_array = '\n\tOverall_Workloads : constant array (1 .. ' + str(taskset.find('tasksetsize').text) + ') of Workloads_Access := (\n'

            get_workload_ada_function = '\t--  Get task "ID" \'s workload for its I-th job release.\n'
            get_workload_ada_function += '\tfunction Get_Workload(ID : Natural; I : Natural) return Positive is\n'
            get_workload_ada_function += '\tbegin\n\t\tif I in Overall_Workloads (ID)\'Range then\n\t\t\treturn Overall_Workloads (ID)(I);\n\t\telse\n\t\t\treturn Overall_Workloads (ID)(0);\n\t\tend if;\n\tend Get_Workload;\n\n'

            workloads_ada_array = {'naming': [], 'value': []}
            
            for core_XML in cores_XML:
              tasks_XML = core_XML.find('tasks')

              current_hyp = max(hyperperiod_core_1, hyperperiod_core_2)

              for task_XML in tasks_XML.findall('task'):
                task_index = int(task_XML.find('ID').text)

                workload_manager_unit += '\tWorkloads_T' + str(task_index) + ' : aliased Workloads := ('

                number_of_JR = int(current_hyp // to_microseconds_for_Ada (task_XML.find('period').text))
                values_for_job_release = []

                # Workloads computation for each job release for current task.
                if task_XML.find('criticality').text == 'HIGH' and ((core_XML.tag == 'core1' and taskset.find('migonc2').text == 'TRUE') or (core_XML.tag == 'core2' and taskset.find('migonc1').text == 'TRUE')):
                  workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))

                  for i in range (0, number_of_JR-1):
                    has_to_exceed = random.randint(1, 100)
                    if has_to_exceed == 1:
                      criticality_factor = (float(taskset.find('criticalityfactor').text))
                      values_for_job_release.append (int((workload * random.uniform(criticality_factor * 0.85, criticality_factor * 0.9))) + 1)
                    else:
                      values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
                else:
                  workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))

                  if task_XML.find('migrating').text == 'False':
                    for i in range (0, number_of_JR-1):
                      values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
                  else:
                    for i in range (0, number_of_JR-1):
                      values_for_job_release.append (int((workload * random.uniform(0.4, 0.5))) + 1)
                  

                for i in range(0, len(values_for_job_release)):
                  if ((i+1) % 300) == 0: # start a new line in order to avoid compilation issues.
                    workload_manager_unit += '\n\t\t\t\t'
                  if i < len(values_for_job_release)-1:
                    workload_manager_unit += str(values_for_job_release[i]) + ', '
                  else:
                    workload_manager_unit += str(values_for_job_release[i]) + ');\n'
                
                overall_workloads_ada_array += '\t\t' + str(task_index) + ' => Workloads_T' + str(task_index) + '\'Access'
                if task_printed != (int(taskset.find('tasksetsize').text) - 1):
                  overall_workloads_ada_array += ',\n'
                else:
                  overall_workloads_ada_array += '\n\t);\n\n'
                task_printed += 1

            # Save everything

            taskset_dir = config.Ada_Paths[experiment_id][approach] + taskset_name + '_v' + str(repetition_id)
            os.mkdir(taskset_dir)

            # dir containing src code
            src_dir = taskset_dir + '/src/'
            os.mkdir(src_dir)
            # dir containing compiled code
            object_code_dir = taskset_dir + '/obj/'
            os.mkdir(object_code_dir)
            # .gpr file
            f = open(taskset_dir + '/' + project_file_name, 'w')
            f.write(project)
            f.close()
            # Makefile
            f = open(taskset_dir + '/makefile', 'w')
            f.write(makefile)
            f.close()
            # taskset unit Ada file
            f = open(src_dir + '/' + file_name, 'w')
            f.write(Ada_Unit)
            f.close()
            # main unit Ada file
            f = open(src_dir + '/' + main_file_name, 'w')
            f.write(Main_Unit)
            f.close()
            # Single_Execution_Data unit file
            f = open(src_dir + '/' + 'single_execution_data.ads', 'w')
            f.write(single_execution_data_unit)
            f.close()

            # Workload_Manager file unit generation
            workload_manager_unit += overall_workloads_ada_array + get_workload_ada_function + 'end Workload_Manager;'
            f = open(src_dir + '/' + 'workload_manager.adb', 'w')
            f.write(workload_manager_unit)
            f.close()
            # flash script and board init file
            f = open(taskset_dir + '/cora_xsdb.ini', 'a')
            f.write('dow ' + 'obj/main_' + taskset_name + '\ncon\nafter ' + str( int(max(hyperperiod_core_1, hyperperiod_core_2)/1000)+5000))
            f.close()
            template_cora_xsdb_file = './Ada_tasksets/template_cora_xsdb.ini'
            cora_ps7_init_file = './Ada_tasksets/cora_ps7_init.tcl'
            copyfile(template_cora_xsdb_file, taskset_dir + '/cora_xsdb.ini')
            copyfile(cora_ps7_init_file, taskset_dir + '/cora_ps7_init.tcl')
            f = open(taskset_dir + '/cora_xsdb.ini', 'a')
            f.write('dow ' + 'obj/main_' + taskset_name + '\ncon\nafter ' + str( int(max(hyperperiod_core_1, hyperperiod_core_2)/1000)+5000))
            f.close()
        else:
          single_execution_data_unit = ''
          single_execution_data_withed_package = 'with System.Multiprocessors;\nuse System.Multiprocessors;\n\n' 
          single_execution_data_unit += single_execution_data_withed_package + 'package Single_Execution_Data is\n\tpragma Preelaborate;\n\n'
          single_execution_data_spec = '\tExperiment_Hyperperiods : array (CPU) of Natural := (CPU\'First => ' + str(hyperperiod_core_1) + ', CPU\'Last => ' + str(hyperperiod_core_2) + ');\n\n'
          # single_execution_data_spec = '\tExperiment_Hyperperiod_CPU_1 : Natural := ' + str(hyperperiod_core_1) + ';\n\n\tExperiment_Hyperperiod_CPU_2 : Natural := ' + str(hyperperiod_core_2) + ';\n\n'

          single_execution_data_spec += '\tId_Experiment : Integer := ' + str(experiment_id) + ';\n\tApproach : String := "' + approach.upper() + '";\n\tTaskset_Id : Integer := ' + str(taskset_id) + ';\n\n'

          single_execution_data_spec += '\tId_Execution : String := "' + taskset_name + '";\n\n'

          data_for_plotting = '\t--  Needed to plot diagrams. These data are stored as strings in order to avoid issue related\n'
          data_for_plotting += '\t--  to differents types representations in differents languages (Python and Ada).\n'
          taskset_size = str(taskset.find('tasksetsize').text)
          taskset_utilization = str(taskset.find('tasksetutilization').text)
          criticality_factor = str(taskset.find('criticalityfactor').text)
          hi_crit_proportion = str(taskset.find('perc').text)
          
          data_for_plotting += '\tTaskset_Size : String := "' + taskset_size + '";\n\tTaskset_Utilization : String := "' + taskset_utilization + '";\n\tCriticality_Factor : String := "' + criticality_factor + '";\n\tHI_Crit_Proportion : String := "' + hi_crit_proportion + '";\n\n'

          single_execution_data_spec += data_for_plotting
          single_execution_data_unit += single_execution_data_spec + 'end Single_Execution_Data;'
          # Workload_Manager body generation
          workload_manager_unit = 'package body Workload_Manager is\n\n\ttype Workloads is array (Natural range <>) of Positive;\n\ttype Workloads_Access is access all Workloads;\n\n'

          overall_workloads_ada_array = '\n\tOverall_Workloads : constant array (1 .. ' + str(taskset.find('tasksetsize').text) + ') of Workloads_Access := (\n'

          get_workload_ada_function = '\t--  Get task "ID" \'s workload for its I-th job release.\n'
          get_workload_ada_function += '\tfunction Get_Workload(ID : Natural; I : Natural) return Positive is\n'
          get_workload_ada_function += '\tbegin\n\t\tif I in Overall_Workloads (ID)\'Range then\n\t\t\treturn Overall_Workloads (ID)(I);\n\t\telse\n\t\t\treturn Overall_Workloads (ID)(0);\n\t\tend if;\n\tend Get_Workload;\n\n'

          workloads_ada_array = {'naming': [], 'value': []}
          
          for core_XML in cores_XML:
            tasks_XML = core_XML.find('tasks')

            current_hyp = max(hyperperiod_core_1, hyperperiod_core_2)

            for task_XML in tasks_XML.findall('task'):
              task_index = int(task_XML.find('ID').text)

              workload_manager_unit += '\tWorkloads_T' + str(task_index) + ' : aliased Workloads := ('

              number_of_JR = int(current_hyp // to_microseconds_for_Ada (task_XML.find('period').text))
              values_for_job_release = []

              # Workloads computation for each job release for current task.
              if task_XML.find('criticality').text == 'HIGH' and ((core_XML.tag == 'core1' and taskset.find('migonc2').text == 'TRUE') or (core_XML.tag == 'core2' and taskset.find('migonc1').text == 'TRUE')):
                workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))
                if experiment_id == 4:
                  higher_bound_exceeding_distribution = 200
                else:
                  higher_bound_exceeding_distribution = 100
                for i in range (0, number_of_JR-1):
                  has_to_exceed = random.randint(1, higher_bound_exceeding_distribution)
                  if has_to_exceed == 1:
                    criticality_factor = (float(taskset.find('criticalityfactor').text))
                    values_for_job_release.append (int((workload * random.uniform(criticality_factor * 0.85, criticality_factor * 0.9))) + 1)
                  else:
                    values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
              else:
                workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))

                if task_XML.find('migrating').text == 'False':
                  for i in range (0, number_of_JR-1):
                    values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
                else:
                  for i in range (0, number_of_JR-1):
                    values_for_job_release.append (int((workload * random.uniform(0.4, 0.5))) + 1)
                

              for i in range(0, len(values_for_job_release)):
                if ((i+1) % 300) == 0: # start a new line in order to avoid compilation issues.
                  workload_manager_unit += '\n\t\t\t\t'
                if i < len(values_for_job_release)-1:
                  workload_manager_unit += str(values_for_job_release[i]) + ', '
                else:
                  workload_manager_unit += str(values_for_job_release[i]) + ');\n'
              
              overall_workloads_ada_array += '\t\t' + str(task_index) + ' => Workloads_T' + str(task_index) + '\'Access'
              if task_printed != (int(taskset.find('tasksetsize').text) - 1):
                overall_workloads_ada_array += ',\n'
              else:
                overall_workloads_ada_array += '\n\t);\n\n'
              task_printed += 1

          # Save everything

          taskset_dir = config.Ada_Paths[experiment_id][approach] + taskset_name
          os.mkdir(taskset_dir)

          # dir containing src code
          src_dir = taskset_dir + '/src/'
          os.mkdir(src_dir)
          # dir containing compiled code
          object_code_dir = taskset_dir + '/obj/'
          os.mkdir(object_code_dir)
          # .gpr file
          f = open(taskset_dir + '/' + project_file_name, 'w')
          f.write(project)
          f.close()
          # Makefile
          f = open(taskset_dir + '/makefile', 'w')
          f.write(makefile)
          f.close()
          # taskset unit Ada file
          f = open(src_dir + '/' + file_name, 'w')
          f.write(Ada_Unit)
          f.close()
          # main unit Ada file
          f = open(src_dir + '/' + main_file_name, 'w')
          f.write(Main_Unit)
          f.close()
          # Single_Execution_Data unit file
          f = open(src_dir + '/' + 'single_execution_data.ads', 'w')
          f.write(single_execution_data_unit)
          f.close()

          # Workload_Manager file unit generation
          workload_manager_unit += overall_workloads_ada_array + get_workload_ada_function + 'end Workload_Manager;'
          f = open(src_dir + '/' + 'workload_manager.adb', 'w')
          f.write(workload_manager_unit)
          f.close()
          # flash script and board init file
          f = open(taskset_dir + '/cora_xsdb.ini', 'a')
          f.write('dow ' + 'obj/main_' + taskset_name + '\ncon\nafter ' + str( int(max(hyperperiod_core_1, hyperperiod_core_2)/1000)+5000))
          f.close()
          template_cora_xsdb_file = './Ada_tasksets/template_cora_xsdb.ini'
          cora_ps7_init_file = './Ada_tasksets/cora_ps7_init.tcl'
          copyfile(template_cora_xsdb_file, taskset_dir + '/cora_xsdb.ini')
          copyfile(cora_ps7_init_file, taskset_dir + '/cora_ps7_init.tcl')
          f = open(taskset_dir + '/cora_xsdb.ini', 'a')
          f.write('dow ' + 'obj/main_' + taskset_name + '\ncon\nafter ' + str( int(max(hyperperiod_core_1, hyperperiod_core_2)/1000)+5000))
          f.close()

# generate a GPR project compiling with Ravenscar with no supporting for migrations
def save_taskset_as_Ada_NO_MIG (experiment_id):
  q = 0
  string_tasks = []

  for approach in config.XML_Files[experiment_id]:
    tree = ET.parse(config.XML_Files[experiment_id][approach])
    root = tree.getroot()

    for taskset in root.findall('taskset'):
      periods_c1 = [] # needed for hyperperiod computations
      periods_c2 = []

      taskset_id = int(taskset.find('tasksetid').text)
      if taskset_id != -1:
        Ada_Unit = ''
        Main_Unit = ''

        taskset_name = taskset.find('executionid').text

        # Main generation
        main_name = 'main_' + taskset_name
        main_file_name = main_name + '.adb'
        main_withed_units = 'with System;\nwith Periodic_Tasks;\n\nwith taskset_' + taskset_name + ';\n' 
        main_unreferenced_units = 'pragma Unreferenced (taskset_'  + taskset_name + ');\n\n'
        main_procedure = 'procedure ' + main_name + ' is\n'
        main_decl_section = "    pragma Priority (System.Priority'Last);\n    pragma CPU (1);\n"
        main_body = 'begin\n    Periodic_Tasks.Init;\nend ' + main_name + ';'
        
        Main_Unit += main_withed_units + main_unreferenced_units +  main_procedure + main_decl_section + main_body

        taskset_dir = config.Ada_No_Mig_Paths[experiment_id][approach] + taskset_name + '/'
        os.mkdir(taskset_dir)

        # dir containing src code
        src_dir = taskset_dir + 'src/'
        os.mkdir(src_dir)
        # dir containing compiled code
        object_code_dir = taskset_dir + 'obj/'
        os.mkdir(object_code_dir)

        # .gpr file project generation
        project_file_name = taskset_name + '.gpr'
        project = 'project ' + taskset_name + ' is\n\n'
        project += '\tfor Languages use ("ada");\n\tfor Main use ("' + main_file_name + '");\n\tfor Source_Dirs use ("src", "../../../common");\n\tfor Object_Dir use "obj";\n    for Runtime ("ada") use '
        runtime_dir = config.RUNTIME_NO_MIG_DIR + ';\n'
        project += runtime_dir + '\tfor Target use "arm-eabi";\n\n'
        project += '\tpackage Compiler is\n        for Switches ("ada") use ("-g", "-gnatwa", "-gnatQ");\n    end Compiler;\n\n'
        project += '\tpackage Builder is\n        for Switches ("ada") use ("-g", "-O0");\n    end Builder;\n\n'
        project += 'end ' + taskset_name + ';'

        f = open(taskset_dir + project_file_name, 'w')
        f.write(project)
        f.close()

        # Makefile generation

        make_all = 'all:  test\n\n'
        make_test = 'test:\n\tgprbuild ' + project_file_name + '\n\n'
        make_clean = 'clean:\n\tgprclean ' + project_file_name + '\n\n'
        makefile = make_all + make_test + make_clean

        f = open(taskset_dir + 'makefile', 'w')
        f.write(makefile)
        f.close()

        # Ada taskset unit generation

        withed_unit = 'with Periodic_Tasks;\nuse Periodic_Tasks;\n'
        package_name = '\npackage taskset_' + taskset_name + ' is\n\n'
        file_name = 'taskset_' + taskset_name + '.ads'

        Ada_Unit += withed_unit + package_name

        cores_XML = [taskset.find('core1'), taskset.find('core2')]

        task_printed = 0
        for core_XML in cores_XML:
          tasks_XML = core_XML.find('tasks')
          
          for task_XML in tasks_XML.findall('task'):
            current_task = '  T_'
            current_task += task_XML.find('ID').text + ' : '

            if task_XML.find('criticality').text == 'HIGH':
              current_task += 'High_Crit ('
              workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CHI').text)))
            else:
              current_task += 'Low_Crit ('
              workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))
            
            current_task += 'Id => ' + task_XML.find('ID').text + ', '

            if core_XML == taskset.find('core2'):
              current_task += 'Pri => ' + str(int(task_XML.find('priority').text)+q) + ', '
              current_task += 'Hosting_Migrating_Tasks_Priority => ' + str(int(task_XML.find('hostingmigpriority').text)+q) + ', '
            else:
              current_task += 'Pri => ' + task_XML.find('priority').text + ', '
              current_task += 'Hosting_Migrating_Tasks_Priority => ' + task_XML.find('hostingmigpriority').text + ', '

            if task_XML.find('criticality').text == 'LOW':
              if core_XML == taskset.find('core1'):
                current_task += 'On_Target_Core_Priority => ' + str(int(task_XML.find('targetpriority').text)+q) + ', '
              else:
                current_task += 'On_Target_Core_Priority => ' + task_XML.find('targetpriority').text + ', '
            
            current_task += 'Low_Critical_Budget => ' + str(to_microseconds_for_Ada (task_XML.find('CLO').text)) + ', '

            if task_XML.find('criticality').text == 'HIGH':
              current_task += 'High_Critical_Budget => ' + str(to_microseconds_for_Ada (task_XML.find('CHI').text)) + ', '
            else:
              current_task += 'Is_Migrable => ' + task_XML.find('migrating').text + ', '
            
            current_task += 'Workload => ' + str(workload) + ', ' # + task_XML.find('workload').text + ', '
            current_task += 'Period => ' + str(to_microseconds_for_Ada (task_XML.find('period').text)) + ', '
            current_task += 'Reduced_Deadline => ' + str(to_microseconds_for_Ada (task_XML.find('reduceddead').text)) + ', '

            if task_XML.find('criticality').text == 'HIGH':
              if (core_XML.tag == 'core1' and taskset.find('migonc2').text == 'TRUE') or (core_XML.tag == 'core2' and taskset.find('migonc1').text == 'TRUE'):
                current_task += 'Could_Exceed => True, '
              else:
                current_task += 'Could_Exceed => False, '

            current_task += 'CPU_Id => ' + ('1' if core_XML.tag == 'core1' else '2') + ');'

            if task_XML.find('migrating').text == "True":
              periods_c1.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))
              periods_c2.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))
            else:
              if core_XML == taskset.find('core1'):
                periods_c1.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))
              else:
                periods_c2.append(int(to_microseconds_for_Ada (task_XML.find('period').text)))

            Ada_Unit += current_task + '\n'

            string_tasks.append(current_task)
            # print(current_task)

        Ada_Unit += '\nend taskset_' + taskset_name + ';\n'
        # create taskset unit Ada file
        f = open(src_dir + file_name, 'w')
        f.write(Ada_Unit)
        f.close()
        # create main unit Ada file
        f = open(src_dir + main_file_name, 'w')
        f.write(Main_Unit)
        f.close()

        # Single_Execution_Data unit generation.
        # This unit contains specifics data for the current tasksets.
        # E.g. Tasksets hyperperiod
        
        hyperperiod_core_1 = int(compute_hyperperiod(periods_c1))
        hyperperiod_core_2 = int(compute_hyperperiod(periods_c2))

        single_execution_data_unit = ''
        single_execution_data_withed_package = 'with System.Multiprocessors;\nuse System.Multiprocessors;\n\n' 
        single_execution_data_unit += single_execution_data_withed_package + 'package Single_Execution_Data is\n\tpragma Preelaborate;\n\n'
        single_execution_data_spec = '\tExperiment_Hyperperiods : array (CPU) of Natural := (CPU\'First => ' + str(hyperperiod_core_1) + ', CPU\'Last => ' + str(hyperperiod_core_2) + ');\n\n'
        # single_execution_data_spec = '\tExperiment_Hyperperiod_CPU_1 : Natural := ' + str(hyperperiod_core_1) + ';\n\n\tExperiment_Hyperperiod_CPU_2 : Natural := ' + str(hyperperiod_core_2) + ';\n\n'

        single_execution_data_spec += '\tId_Experiment : Integer := ' + str(experiment_id) + ';\n\tApproach : String := "' + approach.upper() + '";\n\tTaskset_Id : Integer := ' + str(taskset_id) + ';\n\n'

        single_execution_data_spec += '\tId_Execution : String := "' + taskset_name + '";\n\n'

        data_for_plotting = '\t--  Needed to plot diagrams. These data are stored as strings in order to avoid issue related\n'
        data_for_plotting += '\t--  to differents types representations in differents languages (Python and Ada).\n'
        taskset_size = str(taskset.find('tasksetsize').text)
        taskset_utilization = str(taskset.find('tasksetutilization').text)
        criticality_factor = str(taskset.find('criticalityfactor').text)
        hi_crit_proportion = str(taskset.find('perc').text)
        
        data_for_plotting += '\tTaskset_Size : String := "' + taskset_size + '";\n\tTaskset_Utilization : String := "' + taskset_utilization + '";\n\tCriticality_Factor : String := "' + criticality_factor + '";\n\tHI_Crit_Proportion : String := "' + hi_crit_proportion + '";\n\n'

        single_execution_data_spec += data_for_plotting
        single_execution_data_unit += single_execution_data_spec + 'end Single_Execution_Data;'

        f = open(src_dir + 'single_execution_data.ads', 'w')
        f.write(single_execution_data_unit)
        f.close()

        # flash script and board init file
        
        template_cora_xsdb_file = './Ada_tasksets/template_cora_xsdb.ini'
        cora_ps7_init_file = './Ada_tasksets/cora_ps7_init.tcl'
        copyfile(template_cora_xsdb_file, taskset_dir + 'cora_xsdb.ini')
        copyfile(cora_ps7_init_file, taskset_dir + 'cora_ps7_init.tcl')

        f = open(taskset_dir + 'cora_xsdb.ini', 'a')
        f.write('dow ' + 'obj/main_' + taskset_name + '\ncon\nafter ' + str( int(max(hyperperiod_core_1, hyperperiod_core_2)/1000)+5000))
        f.close()

        # Workload_Manager body generation
        workload_manager_unit = 'package body Workload_Manager is\n\n\ttype Workloads is array (Natural range <>) of Positive;\n\ttype Workloads_Access is access all Workloads;\n\n'

        overall_workloads_ada_array = '\n\tOverall_Workloads : constant array (1 .. ' + str(taskset.find('tasksetsize').text) + ') of Workloads_Access := (\n'

        get_workload_ada_function = '\t--  Get task "ID" \'s workload for its I-th job release.\n'
        get_workload_ada_function += '\tfunction Get_Workload(ID : Natural; I : Natural) return Positive is\n'
        get_workload_ada_function += '\tbegin\n\t\tif I in Overall_Workloads (ID)\'Range then\n\t\t\treturn Overall_Workloads (ID)(I);\n\t\telse\n\t\t\treturn Overall_Workloads (ID)(0);\n\t\tend if;\n\tend Get_Workload;\n\n'

        workloads_ada_array = {'naming': [], 'value': []}
        
        for core_XML in cores_XML:
          tasks_XML = core_XML.find('tasks')

          current_hyp = max(hyperperiod_core_1, hyperperiod_core_2)

          for task_XML in tasks_XML.findall('task'):
            task_index = int(task_XML.find('ID').text)

            workload_manager_unit += '\tWorkloads_T' + str(task_index) + ' : aliased Workloads := ('

            number_of_JR = int(current_hyp // to_microseconds_for_Ada (task_XML.find('period').text))
            values_for_job_release = []

            # Workloads computation for each job release for current task.
            if task_XML.find('criticality').text == 'HIGH' and ((core_XML.tag == 'core1' and taskset.find('migonc2').text == 'TRUE') or (core_XML.tag == 'core2' and taskset.find('migonc1').text == 'TRUE')):
              workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CHI').text)))
          
              for i in range (0, number_of_JR-1):
                has_to_exceed = random.randint(1, 100)
                if has_to_exceed == 1:
                  criticality_factor = (float(taskset.find('criticalityfactor').text))
                  values_for_job_release.append (int((workload * random.uniform(1.2, criticality_factor * 0.8))) + 1)
                else:
                  values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
            else:
              workload = microseconds_to_kilowhetstone_for_ravenscar_runtime( to_microseconds_for_Ada (float(task_XML.find('CLO').text)))

              if task_XML.find('migrating').text == 'False':
                for i in range (0, number_of_JR-1):
                  values_for_job_release.append (int((workload * random.uniform(0.8, 0.9))) + 1)
              else:
                for i in range (0, number_of_JR-1):
                  values_for_job_release.append (int((workload * random.uniform(0.1, 0.11))) + 1)
              

            for i in range(0, len(values_for_job_release)):
              if ((i+1) % 300) == 0: # start a new line in order to avoid compilation issues.
                workload_manager_unit += '\n\t\t\t\t'
              if i < len(values_for_job_release)-1:
                workload_manager_unit += str(values_for_job_release[i]) + ', '
              else:
                workload_manager_unit += str(values_for_job_release[i]) + ');\n'
            
            overall_workloads_ada_array += '\t\t' + str(task_index) + ' => Workloads_T' + str(task_index) + '\'Access'
            if task_printed != (int(taskset.find('tasksetsize').text) - 1):
              overall_workloads_ada_array += ',\n'
            else:
              overall_workloads_ada_array += '\n\t);\n\n'
            task_printed += 1

        # Workload_Manager file unit generation
        workload_manager_unit += overall_workloads_ada_array + get_workload_ada_function + 'end Workload_Manager;'
        f = open(src_dir + 'workload_manager.adb', 'w')
        f.write(workload_manager_unit)
        f.close()

def save_taskset_as_XML (c1_steady, c2_steady, c1_with_mig, c2_with_mig, approach, experiment_id, taskset_U, criticality_factor, hi_crit_proportion, util_on_c1, util_on_c2, taskset_id):
  number_of_cores = 2
  cores_indexes = ['c1', 'c2']
  is_c1_hosting_mig = False
  is_c2_hosting_mig = False

  # assert(len(c1_with_mig) + len(c2_with_mig) > 0), "We have to save only those tasksets concerning at least one migrating task."
  
  if len(c1_with_mig) > 0:
    is_c1_hosting_mig = True
  if len(c2_with_mig) > 0:
    is_c2_hosting_mig = True

  cores_steady = [c1_steady, c2_steady]
  cores_with_mig = [c1_with_mig, c2_with_mig]

  cores = [[], []]
  utilizations_XML = [[], []]
  tasks_XML = [[], []]

  tree = ET.parse(config.XML_Files[experiment_id][approach])
  root = tree.getroot()

  taskset_selector_XML = ET.SubElement(root, 'taskset')

  tasksetid_XML = ET.SubElement(taskset_selector_XML, 'tasksetid')
  tasksetid_XML.text = str(taskset_id)

  executionid_XML = ET.SubElement(taskset_selector_XML, 'executionid')
  executionid_XML.text = ('E' + str(experiment_id) + '_' + approach + '_T' + str(taskset_id)).lower()

  size_XML = ET.SubElement(taskset_selector_XML, 'tasksetsize')
  size_XML.text = str(len(c1_steady) + len(c2_steady))

  util_XML = ET.SubElement(taskset_selector_XML, 'tasksetutilization')
  util_XML.text = str(taskset_U)

  criticality_factor_XML = ET.SubElement(taskset_selector_XML, 'criticalityfactor')
  criticality_factor_XML.text = str(criticality_factor)

  # proportion of HI-crit tasks
  perc_XML = ET.SubElement(taskset_selector_XML, 'perc')
  perc_XML.text = str(hi_crit_proportion)

  is_c1_hosting_mig_XML = ET.SubElement(taskset_selector_XML, 'migonc1')
  is_c1_hosting_mig_XML.text = str(is_c1_hosting_mig).upper()

  is_c2_hosting_mig_XML = ET.SubElement(taskset_selector_XML, 'migonc2')
  is_c2_hosting_mig_XML.text = str(is_c2_hosting_mig).upper()

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

      ID_XML = ET.SubElement(task_XML, 'ID')
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
      reduceddead_XML.text = str(task['D1']) if 'D1' in task else str(task['D'])

      jitter_XML = ET.SubElement(task_XML, 'jitter')
      jitter_XML.text = str(task['J'])

      is_migrating_XML = ET.SubElement(task_XML, 'migrating')
      is_migrating_XML.text = str(task['migrating'])

      priority_XML = ET.SubElement(task_XML, 'priority')
      priority_XML.text = str((task['P'][cores_indexes[i]]))

      hostingmigpriority_XML = ET.SubElement(task_XML, 'hostingmigpriority')
      hostingmigpriority_XML.text = str((task['P']['hosting_migrating'])) if 'hosting_migrating' in task['P'] else str(-1)

      targetpriority_XML = ET.SubElement(task_XML, 'targetpriority')
      targetpriority_XML.text = str((task['P'][cores_indexes[index_other_core]]))

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

def check_size_taskset_with_mig (total, approach, experiment_id, taskset_utilization, criticality_factor, hi_crit_proportion, taskset_id):
  assert(len(config.last_time_on_core_i['c1']) + len(config.last_time_on_core_i['c2']) == total), "Wrong number of scheduled tasks"
  # print_taskset (config.last_time_on_core_i['c1'], config.last_time_on_core_i['c2'])
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
      # print('c2 should NOT have migrating tasks')
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
      # print('c1 should NOT have migrating tasks')
      # @TODO: you are cheating...
      config.last_time_on_core_i_with_additional_migrating_task['c1'] = []

  # we save tasksets belonging to "nomigration" approach in order to make TSV vs MCS comparison.
  if (mig_on_c_i['c1'] or mig_on_c_i['c2']) or approach == 'nomigration':
    # print(approach)
    # check_order_preservation(config.last_time_on_core_i['c1'], config.last_time_on_core_i['c2'], config.last_time_on_core_i_with_additional_migrating_task['c1'], config.last_time_on_core_i_with_additional_migrating_task['c2'])
    # print_taskset (config.last_time_on_core_i['c1'], config.last_time_on_core_i['c2'])
    # print("---")
    save_taskset_as_XML(config.last_time_on_core_i['c1'], config.last_time_on_core_i['c2'], config.last_time_on_core_i_with_additional_migrating_task['c1'], config.last_time_on_core_i_with_additional_migrating_task['c2'], approach, experiment_id, taskset_utilization, criticality_factor, hi_crit_proportion, util_on_core_i['c1'], util_on_core_i['c2'], taskset_id)

# It checks if c_i_steady has the same "tasks order relationship" of c_i_with_mig
def check_order_preservation(c1_steady, c2_steady, c1_with_mig, c2_with_mig):
  '''cores_indexes = ['c1', 'c2']
  c_i_steady = {'c1': c1_steady, 'c2': c2_steady}
  c_i_with_migs = {'c1': c1_with_mig, 'c2': c2_with_mig}
  c_i_migs = {'c1': [], 'c2': []}
  for core in cores_indexes
    if core == 'c1':
      other_core = 'c2'
    else:
      other_core = 'c1'
  if len(c_i_with_migs[core]) > 0:
    # get c_other_core's migrating tasks.
    for task in c_i_steady[other_core]:
      if task['migrating']:
        c_i_mig[other_core].append([task['ID'], task['P']])'''

def beautify_XML_Files(experiment_id):
  for path in config.XML_Files[experiment_id]:
    with open(config.XML_Files[experiment_id][path], "r") as xmldata:
      parsing = xml.dom.minidom.parseString(xmldata.read())  # or xml.dom.minidom.parseString(xml_string)
      xml_pretty_str = parsing.toprettyxml()
      xmldata.close()

    with open(config.XML_Files[experiment_id][path], "w") as xmldata:
      xmldata.write(xml_pretty_str)
      xmldata.close()




