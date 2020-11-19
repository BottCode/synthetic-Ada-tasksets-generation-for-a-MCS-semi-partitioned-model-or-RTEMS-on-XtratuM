with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2239 is
begin

  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 56.86079311049145, High_Critical_Budget => 113.7215862209829, Workload => 0, Period => 300, CPU_Id => 1);
  T_4 : High_Crit (Pri => 1, Low_Critical_Budget => 1.2143354579950771, High_Critical_Budget => 2.4286709159901543, Workload => 0, Period => 40, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 2, Low_Critical_Budget => 4.479798501992899, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 3, Low_Critical_Budget => 1.8246423953125945, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_7 : High_Crit (Pri => 0, Low_Critical_Budget => 102.74387221076785, High_Critical_Budget => 205.4877444215357, Workload => 0, Period => 680, CPU_Id => 2);
  T_1 : High_Crit (Pri => 3, Low_Critical_Budget => 0.5310345095454116, High_Critical_Budget => 1.0620690190908233, Workload => 0, Period => 10, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 57.0901228728018, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 1, Low_Critical_Budget => 45.63056894399665, Is_Migrable => True, Workload => 0, Period => 340, CPU_Id => 2);

end E4_semi1WF_T2239;
