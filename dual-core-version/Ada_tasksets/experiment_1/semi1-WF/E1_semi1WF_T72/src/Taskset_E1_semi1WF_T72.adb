with Periodic_Tasks;

package body Taskset_E1_semi1WF_T72 is
begin

  Periodic_Tasks.Experiment_Hyperperiod :=  1_000_000;

  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 2.170986965210069, High_Critical_Budget => 4.341973930420138, Workload => 0, Period => 20, CPU_Id => 1);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 1.4368605724228034, High_Critical_Budget => 2.873721144845607, Workload => 0, Period => 20, CPU_Id => 1);
  T_6 : High_Crit (Pri => 4, Low_Critical_Budget => 0.04422046826177972, High_Critical_Budget => 0.08844093652355944, Workload => 0, Period => 20, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 1, Low_Critical_Budget => 203.46373706420343, Is_Migrable => False, Workload => 0, Period => 340, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 0, Low_Critical_Budget => 56.131661531951174, Is_Migrable => True, Workload => 0, Period => 530, CPU_Id => 1);
  T_3 : High_Crit (Pri => 2, Low_Critical_Budget => 0.8906978728989706, High_Critical_Budget => 1.7813957457979412, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : High_Crit (Pri => 3, Low_Critical_Budget => 0.8052886307146384, High_Critical_Budget => 1.6105772614292768, Workload => 0, Period => 10, CPU_Id => 2);
  T_5 : High_Crit (Pri => 1, Low_Critical_Budget => 2.684382881902958, High_Critical_Budget => 5.368765763805916, Workload => 0, Period => 80, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 0, Low_Critical_Budget => 195.2652456964417, Is_Migrable => False, Workload => 0, Period => 570, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.5666749186036433, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.846631769342604, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.671298864369964, Is_Migrable => False, Workload => 0, Period => 160, CPU_Id => 2);

end E1_semi1WF_T72;
