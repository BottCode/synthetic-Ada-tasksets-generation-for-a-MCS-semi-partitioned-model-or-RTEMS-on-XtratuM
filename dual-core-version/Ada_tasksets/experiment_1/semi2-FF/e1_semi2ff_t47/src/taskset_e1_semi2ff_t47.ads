with Periodic_Tasks;
use Periodic_Tasks;

package taskset_e1_semi2ff_t47 is

  T_5 : High_Crit (Pri => 4, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 10, CPU_Id => 1);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 40, CPU_Id => 1);
  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 350, CPU_Id => 1);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 430, CPU_Id => 1);
  T_7 : High_Crit (Pri => 0, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 860, CPU_Id => 1);
  T_1 : High_Crit (Pri => 0, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 170, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 3, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 70, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 2, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 180, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 190, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 4, Low_Critical_Budget => 1, Is_Migrable => False, Workload => 1, Period => 70, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 6, Low_Critical_Budget => 1, Is_Migrable => True, Workload => 1, Period => 10, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 5, Low_Critical_Budget => 1, Is_Migrable => True, Workload => 1, Period => 40, CPU_Id => 2);

end taskset_e1_semi2ff_t47;
