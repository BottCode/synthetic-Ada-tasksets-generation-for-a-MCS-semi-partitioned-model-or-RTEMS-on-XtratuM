with Periodic_Tasks;

package body Taskset_E2_semi2WF_T1165 is
begin

  T_8 : High_Crit (Pri => 2, Low_Critical_Budget => 1.9018187731862577, High_Critical_Budget => 7.131820399448467, Workload => 0, Period => 10, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 9.407445954369816, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 0, Low_Critical_Budget => 7.299785342935228, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 0.5197982103078136, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_6 : High_Crit (Pri => 6, Low_Critical_Budget => 1.6985190531747163, High_Critical_Budget => 6.369446449405186, Workload => 0, Period => 50, CPU_Id => 2);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 25.13673262062182, High_Critical_Budget => 94.26274732733182, Workload => 0, Period => 910, CPU_Id => 2);
  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 11.92947627925711, High_Critical_Budget => 44.73553604721416, Workload => 0, Period => 440, CPU_Id => 2);
  T_7 : High_Crit (Pri => 3, Low_Critical_Budget => 3.441139898625523, High_Critical_Budget => 12.904274619845712, Workload => 0, Period => 200, CPU_Id => 2);
  T_10 : High_Crit (Pri => 2, Low_Critical_Budget => 1.436274266882387, High_Critical_Budget => 5.386028500808951, Workload => 0, Period => 330, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 47.92516030402684, Is_Migrable => True, Workload => 0, Period => 160, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 4, Low_Critical_Budget => 44.91809611674975, Is_Migrable => False, Workload => 0, Period => 220, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 7, Low_Critical_Budget => 9.585774684856268, Is_Migrable => True, Workload => 0, Period => 90, CPU_Id => 2);

end E2_semi2WF_T1165;
