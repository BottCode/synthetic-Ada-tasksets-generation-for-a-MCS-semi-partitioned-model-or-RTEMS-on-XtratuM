with Periodic_Tasks;
use Periodic_Tasks;

package taskset_e1_semi2wf_t59 is

  T_2 : High_Crit (Pri => 3, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 160, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 850, CPU_Id => 1);
  T_5 : High_Crit (Pri => 4, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 10, CPU_Id => 1);
  T_11 : High_Crit (Pri => 2, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 180, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 1, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 650, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 10, CPU_Id => 1);
  T_0 : High_Crit (Pri => 0, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 850, CPU_Id => 2);
  T_8 : High_Crit (Pri => 1, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 540, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 120, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 300, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 4, Low_Critical_Budget => 1, Is_Migrable => True, Workload => 1, Period => 60, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 5, Low_Critical_Budget => 1, Is_Migrable => True, Workload => 1, Period => 20, CPU_Id => 2);

end taskset_e1_semi2wf_t59;
