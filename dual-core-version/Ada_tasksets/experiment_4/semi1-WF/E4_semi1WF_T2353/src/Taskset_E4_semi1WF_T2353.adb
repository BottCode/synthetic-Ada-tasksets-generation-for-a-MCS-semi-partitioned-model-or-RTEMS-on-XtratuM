with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2353 is
begin

  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 21.2773482581417, High_Critical_Budget => 42.5546965162834, Workload => 0, Period => 70, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 1, Low_Critical_Budget => 86.48865123867725, Is_Migrable => False, Workload => 0, Period => 270, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 0, Low_Critical_Budget => 0.5120021847949996, Is_Migrable => False, Workload => 0, Period => 460, CPU_Id => 1);
  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 1.5487129565748758, High_Critical_Budget => 3.0974259131497517, Workload => 0, Period => 10, CPU_Id => 2);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 3.1233986976102868, High_Critical_Budget => 6.2467973952205735, Workload => 0, Period => 40, CPU_Id => 2);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 8.385330945531255, High_Critical_Budget => 16.77066189106251, Workload => 0, Period => 150, CPU_Id => 2);
  T_8 : High_Crit (Pri => 4, Low_Critical_Budget => 0.20843526324343845, High_Critical_Budget => 0.4168705264868769, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.9057342537457378, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 2, Low_Critical_Budget => 9.104991100933553, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.7149039329026765, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);

end E4_semi1WF_T2353;
