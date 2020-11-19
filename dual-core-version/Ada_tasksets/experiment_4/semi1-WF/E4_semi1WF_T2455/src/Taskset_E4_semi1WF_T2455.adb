with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2455 is
begin

  T_9 : High_Crit (Pri => 2, Low_Critical_Budget => 14.293328076315333, High_Critical_Budget => 28.586656152630667, Workload => 0, Period => 80, CPU_Id => 1);
  T_0 : High_Crit (Pri => 3, Low_Critical_Budget => 3.057027141611419, High_Critical_Budget => 6.114054283222838, Workload => 0, Period => 80, CPU_Id => 1);
  T_4 : High_Crit (Pri => 4, Low_Critical_Budget => 0.33065930113561626, High_Critical_Budget => 0.6613186022712325, Workload => 0, Period => 50, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.5465121181685557, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 78.30351845587886, Is_Migrable => False, Workload => 0, Period => 420, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 0, Low_Critical_Budget => 37.80373710729521, Is_Migrable => False, Workload => 0, Period => 830, CPU_Id => 1);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 4.626173710178562, High_Critical_Budget => 9.252347420357124, Workload => 0, Period => 30, CPU_Id => 2);
  T_2 : High_Crit (Pri => 0, Low_Critical_Budget => 19.795197268151043, High_Critical_Budget => 39.590394536302085, Workload => 0, Period => 380, CPU_Id => 2);
  T_5 : High_Crit (Pri => 4, Low_Critical_Budget => 0.3178117662401958, High_Critical_Budget => 0.6356235324803916, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 1, Low_Critical_Budget => 17.76005170062902, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 13.470790223568045, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.488939298873273, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 2);

end E4_semi1WF_T2455;
