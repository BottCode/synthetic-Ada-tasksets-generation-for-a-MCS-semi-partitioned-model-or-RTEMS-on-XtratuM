with Periodic_Tasks;

package body Taskset_E2_semi2WF_T1260 is
begin

  T_5 : High_Crit (Pri => 1, Low_Critical_Budget => 17.150507542053724, High_Critical_Budget => 68.6020301682149, Workload => 0, Period => 250, CPU_Id => 1);
  T_0 : High_Crit (Pri => 4, Low_Critical_Budget => 0.5559088905284282, High_Critical_Budget => 2.2236355621137127, Workload => 0, Period => 20, CPU_Id => 1);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 10.744907841032349, High_Critical_Budget => 42.979631364129396, Workload => 0, Period => 390, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 5, Low_Critical_Budget => 11.969606303659997, Is_Migrable => True, Workload => 0, Period => 50, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 2, Low_Critical_Budget => 65.1844587507201, Is_Migrable => False, Workload => 0, Period => 460, CPU_Id => 1);
  T_9 : Low_Crit (Pri => 3, Low_Critical_Budget => 27.141387887654805, Is_Migrable => True, Workload => 0, Period => 200, CPU_Id => 1);
  T_6 : High_Crit (Pri => 3, Low_Critical_Budget => 0.6230973646840887, High_Critical_Budget => 2.492389458736355, Workload => 0, Period => 10, CPU_Id => 2);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 2.659529783228707, High_Critical_Budget => 10.638119132914827, Workload => 0, Period => 60, CPU_Id => 2);
  T_4 : High_Crit (Pri => 4, Low_Critical_Budget => 0.1908133082279556, High_Critical_Budget => 0.7632532329118225, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 2, Low_Critical_Budget => 14.639660501895126, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 0, Low_Critical_Budget => 200.27700276066858, Is_Migrable => False, Workload => 0, Period => 970, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.16926108864775802, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);

end E2_semi2WF_T1260;
