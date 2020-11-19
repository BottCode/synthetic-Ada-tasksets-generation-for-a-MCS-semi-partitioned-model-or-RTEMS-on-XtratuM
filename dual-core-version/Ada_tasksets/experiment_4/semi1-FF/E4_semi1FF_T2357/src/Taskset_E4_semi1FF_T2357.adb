with Periodic_Tasks;

package body Taskset_E4_semi1FF_T2357 is
begin

  T_8 : High_Crit (Pri => 1, Low_Critical_Budget => 7.10873450164603, High_Critical_Budget => 14.21746900329206, Workload => 0, Period => 30, CPU_Id => 1);
  T_7 : High_Crit (Pri => 0, Low_Critical_Budget => 22.902595007840993, High_Critical_Budget => 45.80519001568199, Workload => 0, Period => 180, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 1.165392872325438, High_Critical_Budget => 2.330785744650876, Workload => 0, Period => 10, CPU_Id => 1);
  T_9 : High_Crit (Pri => 4, Low_Critical_Budget => 2.0108897327181583, High_Critical_Budget => 4.021779465436317, Workload => 0, Period => 20, CPU_Id => 2);
  T_5 : High_Crit (Pri => 5, Low_Critical_Budget => 0.7739808080263222, High_Critical_Budget => 1.5479616160526444, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 2, Low_Critical_Budget => 29.92882515829399, Is_Migrable => False, Workload => 0, Period => 190, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 1, Low_Critical_Budget => 43.68052739456048, Is_Migrable => False, Workload => 0, Period => 290, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 3, Low_Critical_Budget => 27.6866398310983, Is_Migrable => False, Workload => 0, Period => 190, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.7954903974681278, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 0, Low_Critical_Budget => 100.36095975204786, Is_Migrable => True, Workload => 0, Period => 980, CPU_Id => 2);

end E4_semi1FF_T2357;
