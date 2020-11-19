with Periodic_Tasks;

package body Taskset_E2_semi1FF_T151 is
begin

  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 21.220139057858074, High_Critical_Budget => 26.525173822322593, Workload => 0, Period => 60, CPU_Id => 1);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 68.23930557612279, High_Critical_Budget => 85.29913197015348, Workload => 0, Period => 270, CPU_Id => 1);
  T_8 : High_Crit (Pri => 3, Low_Critical_Budget => 2.5165402905262653, High_Critical_Budget => 3.1456753631578316, Workload => 0, Period => 30, CPU_Id => 1);
  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 0.4746904950647348, High_Critical_Budget => 0.5933631188309185, Workload => 0, Period => 60, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.8295603217456433, Is_Migrable => True, Workload => 0, Period => 30, CPU_Id => 1);
  T_6 : High_Crit (Pri => 4, Low_Critical_Budget => 2.4746027682630407, High_Critical_Budget => 3.0932534603288007, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : High_Crit (Pri => 2, Low_Critical_Budget => 8.276919751081877, High_Critical_Budget => 10.346149688852346, Workload => 0, Period => 50, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 1, Low_Critical_Budget => 77.7727504715214, Is_Migrable => False, Workload => 0, Period => 580, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 3, Low_Critical_Budget => 6.476386269550166, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.367014668863381, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.37417460839535677, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 0, Low_Critical_Budget => 15.680658884112455, Is_Migrable => False, Workload => 0, Period => 980, CPU_Id => 2);

end E2_semi1FF_T151;
