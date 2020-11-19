with Periodic_Tasks;

package body Taskset_E2_semi2FF_T552 is
begin

  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 14.28447763558255, High_Critical_Budget => 32.140074680060735, Workload => 0, Period => 60, CPU_Id => 1);
  T_9 : High_Crit (Pri => 3, Low_Critical_Budget => 2.646626481902859, High_Critical_Budget => 5.954909584281433, Workload => 0, Period => 20, CPU_Id => 1);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 3.8294986151968513, High_Critical_Budget => 8.616371884192915, Workload => 0, Period => 70, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 0.04297295777204527, High_Critical_Budget => 0.09668915498710184, Workload => 0, Period => 40, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.32753765553359626, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_3 : High_Crit (Pri => 5, Low_Critical_Budget => 0.4372263702599503, High_Critical_Budget => 0.9837593330848882, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : High_Crit (Pri => 1, Low_Critical_Budget => 1.818365234771334, High_Critical_Budget => 4.091321778235502, Workload => 0, Period => 100, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 4, Low_Critical_Budget => 19.06556909735558, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 3, Low_Critical_Budget => 15.75267308105131, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 0, Low_Critical_Budget => 33.33571692306083, Is_Migrable => False, Workload => 0, Period => 190, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 2, Low_Critical_Budget => 12.215145689206274, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.08636608363083109, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);

end E2_semi2FF_T552;
