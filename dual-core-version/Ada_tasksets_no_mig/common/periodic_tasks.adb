with Ada.Real_Time; use Ada.Real_Time;
with Ada.Text_IO;

pragma Warnings (Off);
with System;
with System.BB.Time;
use System.BB.Time;
with System.Task_Primitives.Operations;
with System.BB.Threads.Queues;
with System.OS_Interface;
with Core_Execution_Modes;
pragma Warnings (On);

with Ada.Strings.Unbounded;
with Experiment_Info;
with Single_Execution_Data;
with Production_Workload;
with Workload_Manager;
with Initial_Delay;

package body Periodic_Tasks is

   package STPO renames System.Task_Primitives.Operations;

   function Get_Longest_Hyperperiod return Natural is
   begin
      if Single_Execution_Data.Experiment_Hyperperiods (CPU'First) > Single_Execution_Data.Experiment_Hyperperiods (CPU'Last) then
         return Single_Execution_Data.Experiment_Hyperperiods (CPU'First);
      end if;

      return Single_Execution_Data.Experiment_Hyperperiods (CPU'Last);
   end Get_Longest_Hyperperiod;

   ---------------------
   --  type Low_Crit  --
   ---------------------

   task body Low_Crit is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Period);
      I : Natural := 0;
   begin
      STPO.Initialize_LO_Crit_Task (STPO.Self, Id, Hosting_Migrating_Tasks_Priority, On_Target_Core_Priority,
                                    System.BB.Time.Microseconds (Low_Critical_Budget), Period, Reduced_Deadline, Is_Migrable);
      loop
         delay until Next_Period;

         --  Ada.Text_IO.Put_Line ("CPU: " & CPU'Image(System.OS_Interface.Current_CPU) & Integer'Image(ID) & Integer'Image (I));
         Production_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));
         
         I := I + 1;

         Next_Period := Next_Period + Period_To_Add;
      end loop;
   end Low_Crit;

   ----------------------
   --  type High_Crit  --
   ----------------------

   task body High_Crit is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Period);
      I : Natural := 0;
   begin
      STPO.Initialize_HI_Crit_Task
         (STPO.Self, Id, Hosting_Migrating_Tasks_Priority, System.BB.Time.Microseconds (Low_Critical_Budget), System.BB.Time.Microseconds (High_Critical_Budget), Period);

      loop
         delay until Next_Period;
         
         --  Ada.Text_IO.Put_Line ("CPU: " & CPU'Image(System.OS_Interface.Current_CPU) & Integer'Image(ID) & Integer'Image (I));
         Production_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));

         I := I + 1;

         Next_Period := Next_Period + Period_To_Add;
      end loop;
   end High_Crit;

   ------------
   --  Init  --
   ------------

   procedure Init is
      use Ada.Strings.Unbounded;
      Experiment_Parameters : Experiment_Info.Exp_Params;
   begin
      Experiment_Parameters.Experiment_Hyperperiods :=
        (CPU'First => Single_Execution_Data.Experiment_Hyperperiods (CPU'First),
         CPU'Last => Single_Execution_Data.Experiment_Hyperperiods (CPU'Last));
      
      Experiment_Parameters.Id_Experiment := Single_Execution_Data.Id_Experiment;
      Experiment_Parameters.Approach := To_Unbounded_String (Single_Execution_Data.Approach);
      Experiment_Parameters.Taskset_Id := Single_Execution_Data.Taskset_Id;
      Experiment_Parameters.Id_Execution := To_Unbounded_String (Single_Execution_Data.Id_Execution);
      
      Experiment_Info.Set_Parameters (Experiment_Parameters);
      --  Stuck until someone states that experiment is over.
      Core_Execution_Modes.Wait_Experiment_Over;
      --  Ada.Text_IO.Put_Line ("----------------------");
      --  Ada.Text_IO.Put_Line ("--  END EXPERIMENT  --");
      --  Ada.Text_IO.Put_Line ("----------------------");
      Ada.Text_IO.Put_Line("");
      Ada.Text_IO.Put_Line("");

      Ada.Text_IO.Put_Line ("<execution>");
      Ada.Text_IO.Put_Line ("<supportingmigrations>FALSE</supportingmigrations>"); 

      Ada.Text_IO.Put_Line ("<executionid>" & Single_Execution_Data.Id_Execution & "</executionid>");
      Ada.Text_IO.Put_Line ("<experimentid>" & Integer'Image (Single_Execution_Data.Id_Experiment) & "</experimentid>");
      Ada.Text_IO.Put_Line ("<approach>" & Single_Execution_Data.Approach & "</approach>");
      Ada.Text_IO.Put_Line ("<tasksetid>" & Integer'Image (Single_Execution_Data.Taskset_Id) & "</tasksetid>");
      Ada.Text_IO.Put_Line ("<tasksetsize>" & Single_Execution_Data.Taskset_Size & "</tasksetsize>");
      Ada.Text_IO.Put_Line ("<tasksetutilization>" & Single_Execution_Data.Taskset_Utilization & "</tasksetutilization>");
      Ada.Text_IO.Put_Line ("<criticalityfactor>" & Single_Execution_Data.Criticality_Factor & "</criticalityfactor>");
      Ada.Text_IO.Put_Line ("<perc>" & Single_Execution_Data.HI_Crit_Proportion & "</perc>");
      Ada.Text_IO.Put_Line ("<hyperperiodc1>" & Natural'Image (Single_Execution_Data.Experiment_Hyperperiods (CPU'First)) & "</hyperperiodc1>");
      Ada.Text_IO.Put_Line ("<hyperperiodc2>" & Natural'Image (Single_Execution_Data.Experiment_Hyperperiods (CPU'Last)) & "</hyperperiodc2>");

      System.BB.Threads.Queues.Print_Tasks_Log;
      Core_Execution_Modes.Print_CPUs_Log;

      Ada.Text_IO.Put_Line ("</execution>");

      Ada.Text_IO.Put_Line("");
      Ada.Text_IO.Put_Line("");
      --  System.BB.Threads.Queues.Print_Queues;

      loop
         null;
      end loop;
   end Init;

   ----------------------------
   --  End_Task_Second_Core  --
   ----------------------------
   
   --  This task stucks second core's execution when current experiment should stops.
   task End_Task_Second_Core with 
         Priority => System.Priority'Last,
         CPU      => CPU'Last;

   task body End_Task_Second_Core is
   begin
      --  Stuck until someone states that experiment is over.
      Core_Execution_Modes.Wait_Experiment_Over;

      loop
         null;
      end loop;
   end End_Task_Second_Core;

   task Notify_Major_Hyperperiod_Has_Been_Expired with 
         Priority => System.Priority'Last - 1,
         CPU      => CPU'Last;
   
   task body Notify_Major_Hyperperiod_Has_Been_Expired is
      Next_Period : constant Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod);
   begin
      delay until Next_Period + Period_To_Add;

      Core_Execution_Modes.Set_Parameters_Referee
                                       (Safe_Boundary_Exceeded => False,
                                       Experiment_Not_Valid => False,
                                       Finish_Experiment => True);

   end Notify_Major_Hyperperiod_Has_Been_Expired;

end Periodic_Tasks;
