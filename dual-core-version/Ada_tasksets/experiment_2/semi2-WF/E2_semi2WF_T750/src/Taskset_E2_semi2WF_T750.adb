with Periodic_Tasks;

package body Taskset_E2_semi2WF_T750 is
begin

  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 16.267005591965734, High_Critical_Budget => 44.73426537790577, Workload => 0, Period => 160, CPU_Id => 1);
  T_4 : High_Crit (Pri => 4, Low_Critical_Budget => 0.540366629306948, High_Critical_Budget => 1.486008230594107, Workload => 0, Period => 10, CPU_Id => 1);
  T_9 : High_Crit (Pri => 2, Low_Critical_Budget => 0.3629899702508324, High_Critical_Budget => 0.9982224181897892, Workload => 0, Period => 40, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 0, Low_Critical_Budget => 136.0962667291711, Is_Migrable => False, Workload => 0, Period => 420, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 3, Low_Critical_Budget => 19.33353581292932, Is_Migrable => False, Workload => 0, Period => 270, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.49031315396480313, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.06187093722637371, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : High_Crit (Pri => 0, Low_Critical_Budget => 26.699205135784737, High_Critical_Budget => 73.42281412340803, Workload => 0, Period => 320, CPU_Id => 2);
  T_8 : High_Crit (Pri => 2, Low_Critical_Budget => 0.5712040863429703, High_Critical_Budget => 1.5708112374431682, Workload => 0, Period => 10, CPU_Id => 2);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 0.8150597532800578, High_Critical_Budget => 2.2414143215201587, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.758514734217524, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 3, Low_Critical_Budget => 4.681153611434885, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);

end E2_semi2WF_T750;
