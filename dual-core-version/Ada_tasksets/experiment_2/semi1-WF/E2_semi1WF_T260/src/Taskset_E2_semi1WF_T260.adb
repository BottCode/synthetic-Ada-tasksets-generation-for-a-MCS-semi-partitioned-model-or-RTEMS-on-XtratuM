with Periodic_Tasks;

package body Taskset_E2_semi1WF_T260 is
begin

  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 9.744716401036007, High_Critical_Budget => 14.617074601554009, Workload => 0, Period => 30, CPU_Id => 1);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 91.84304176306328, High_Critical_Budget => 137.76456264459492, Workload => 0, Period => 780, CPU_Id => 1);
  T_8 : High_Crit (Pri => 1, Low_Critical_Budget => 9.877795437549839, High_Critical_Budget => 14.816693156324758, Workload => 0, Period => 320, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 2, Low_Critical_Budget => 83.64523575531207, Is_Migrable => False, Workload => 0, Period => 460, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 4, Low_Critical_Budget => 6.37915680662628, Is_Migrable => True, Workload => 0, Period => 90, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.39820846127780685, Is_Migrable => True, Workload => 0, Period => 90, CPU_Id => 1);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 24.09599949830177, High_Critical_Budget => 36.143999247452655, Workload => 0, Period => 80, CPU_Id => 2);
  T_4 : High_Crit (Pri => 3, Low_Critical_Budget => 5.103164727156748, High_Critical_Budget => 7.654747090735122, Workload => 0, Period => 30, CPU_Id => 2);
  T_11 : High_Crit (Pri => 2, Low_Critical_Budget => 0.13003810046569622, High_Critical_Budget => 0.19505715069854435, Workload => 0, Period => 40, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 0, Low_Critical_Budget => 66.90201558383515, Is_Migrable => False, Workload => 0, Period => 420, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 3.530238450753682, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 1.2790873096347877, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 2);

end E2_semi1WF_T260;
