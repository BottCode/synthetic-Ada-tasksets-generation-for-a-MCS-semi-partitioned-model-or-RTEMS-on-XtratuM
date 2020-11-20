with Periodic_Tasks;
use Periodic_Tasks;

package taskset_e1_semi2wf_t51 is

  T_4 : High_Crit (Pri => 2, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 50, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 640, CPU_Id => 1);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 60, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 4, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 20, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 5, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 20, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 6, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 20, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 60, CPU_Id => 1);
  T_11 : High_Crit (Pri => 2, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 230, CPU_Id => 2);
  T_3 : High_Crit (Pri => 1, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 550, CPU_Id => 2);
  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 770, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 3, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 50, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 1, Is_Migrable => True, Workload => 1, Period => 30, CPU_Id => 2);

end taskset_e1_semi2wf_t51;
