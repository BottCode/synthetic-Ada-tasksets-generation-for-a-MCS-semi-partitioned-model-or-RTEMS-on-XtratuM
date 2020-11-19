with Periodic_Tasks;

package body Taskset_E4_semi2WF_T2265 is
begin

  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 3.7763435598695994, High_Critical_Budget => 7.552687119739199, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 1, Low_Critical_Budget => 23.060438112867097, Is_Migrable => False, Workload => 0, Period => 120, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 0, Low_Critical_Budget => 3.2804402583539964, Is_Migrable => False, Workload => 0, Period => 360, CPU_Id => 1);
  T_4 : High_Crit (Pri => 0, Low_Critical_Budget => 35.532325078113416, High_Critical_Budget => 71.06465015622683, Workload => 0, Period => 490, CPU_Id => 2);
  T_3 : High_Crit (Pri => 4, Low_Critical_Budget => 0.574009474186184, High_Critical_Budget => 1.148018948372368, Workload => 0, Period => 10, CPU_Id => 2);
  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 0.626512911175805, High_Critical_Budget => 1.25302582235161, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 82.91145016496839, Is_Migrable => False, Workload => 0, Period => 220, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 3, Low_Critical_Budget => 16.40476620562283, Is_Migrable => True, Workload => 0, Period => 50, CPU_Id => 2);

end E4_semi2WF_T2265;
