with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2286 is
begin

  T_2 : High_Crit (Pri => 0, Low_Critical_Budget => 87.15938494053252, High_Critical_Budget => 174.31876988106504, Workload => 0, Period => 220, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 3.3789668686937024, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 2, Low_Critical_Budget => 1.381384014941256, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 5.07241678478965, High_Critical_Budget => 10.1448335695793, Workload => 0, Period => 30, CPU_Id => 2);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 4.739433066341059, High_Critical_Budget => 9.478866132682118, Workload => 0, Period => 200, CPU_Id => 2);
  T_7 : High_Crit (Pri => 4, Low_Critical_Budget => 0.05717761929153323, High_Critical_Budget => 0.11435523858306645, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 2, Low_Critical_Budget => 29.509319409497547, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 0, Low_Critical_Budget => 199.94471215302994, Is_Migrable => True, Workload => 0, Period => 810, CPU_Id => 2);

end E4_semi1WF_T2286;
