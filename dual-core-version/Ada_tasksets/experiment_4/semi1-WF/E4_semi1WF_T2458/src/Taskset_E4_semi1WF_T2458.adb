with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2458 is
begin

  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 2.1305283938315203, High_Critical_Budget => 4.2610567876630405, Workload => 0, Period => 10, CPU_Id => 1);
  T_4 : High_Crit (Pri => 0, Low_Critical_Budget => 28.67600059772127, High_Critical_Budget => 57.35200119544254, Workload => 0, Period => 930, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 1, Low_Critical_Budget => 140.55233329283018, Is_Migrable => False, Workload => 0, Period => 290, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 2.0606853788177837, Is_Migrable => True, Workload => 0, Period => 80, CPU_Id => 1);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 56.117104719122295, High_Critical_Budget => 112.23420943824459, Workload => 0, Period => 440, CPU_Id => 2);
  T_2 : High_Crit (Pri => 3, Low_Critical_Budget => 2.790116442275521, High_Critical_Budget => 5.580232884551042, Workload => 0, Period => 60, CPU_Id => 2);
  T_9 : High_Crit (Pri => 4, Low_Critical_Budget => 1.5541413847438097, High_Critical_Budget => 3.1082827694876194, Workload => 0, Period => 40, CPU_Id => 2);
  T_0 : High_Crit (Pri => 1, Low_Critical_Budget => 10.602105455231232, High_Critical_Budget => 21.204210910462464, Workload => 0, Period => 290, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 2, Low_Critical_Budget => 112.73858414953598, Is_Migrable => False, Workload => 0, Period => 420, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 7, Low_Critical_Budget => 0.9356309313248962, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.2430545754752578, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.0642080968045375, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);

end E4_semi1WF_T2458;
