with Periodic_Tasks;

package body Taskset_E2_semi1FF_T1152 is
begin

  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 24.10903295054584, High_Critical_Budget => 90.4088735645469, Workload => 0, Period => 180, CPU_Id => 1);
  T_7 : High_Crit (Pri => 3, Low_Critical_Budget => 3.379404947002669, High_Critical_Budget => 12.672768551260008, Workload => 0, Period => 70, CPU_Id => 1);
  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 11.490044171676299, High_Critical_Budget => 43.087665643786124, Workload => 0, Period => 300, CPU_Id => 1);
  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 0.4385477142127172, High_Critical_Budget => 1.6445539282976895, Workload => 0, Period => 90, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 4, Low_Critical_Budget => 3.150042100465118, Is_Migrable => True, Workload => 0, Period => 80, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.134667253725544, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 1);
  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 1.6620480411477332, High_Critical_Budget => 6.232680154303999, Workload => 0, Period => 50, CPU_Id => 2);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 5.234991481813105, High_Critical_Budget => 19.631218056799142, Workload => 0, Period => 300, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 3, Low_Critical_Budget => 4.108671281866787, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 4, Low_Critical_Budget => 1.629485546669447, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.5393460257558766, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 3.0997980018665716, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 2);

end E2_semi1FF_T1152;
