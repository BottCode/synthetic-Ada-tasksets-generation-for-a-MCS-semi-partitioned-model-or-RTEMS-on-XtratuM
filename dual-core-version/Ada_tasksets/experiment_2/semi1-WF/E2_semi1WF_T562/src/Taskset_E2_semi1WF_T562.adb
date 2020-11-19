with Periodic_Tasks;

package body Taskset_E2_semi1WF_T562 is
begin

  T_2 : High_Crit (Pri => 4, Low_Critical_Budget => 3.2939404168874997, High_Critical_Budget => 7.411365937996875, Workload => 0, Period => 30, CPU_Id => 1);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 27.48065687599509, High_Critical_Budget => 61.831477970988956, Workload => 0, Period => 630, CPU_Id => 1);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 6.170690756743821, High_Critical_Budget => 13.884054202673598, Workload => 0, Period => 350, CPU_Id => 1);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 8.224212104950118, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 48.269542778897936, Is_Migrable => False, Workload => 0, Period => 330, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 2, Low_Critical_Budget => 23.905818051056986, Is_Migrable => True, Workload => 0, Period => 480, CPU_Id => 1);
  T_5 : High_Crit (Pri => 2, Low_Critical_Budget => 31.68088314537427, High_Critical_Budget => 71.28198707709211, Workload => 0, Period => 380, CPU_Id => 2);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 48.49937291453961, High_Critical_Budget => 109.12358905771413, Workload => 0, Period => 750, CPU_Id => 2);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 24.214558733085234, High_Critical_Budget => 54.482757149441774, Workload => 0, Period => 890, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 5, Low_Critical_Budget => 23.117883642564152, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 16.943220518485592, Is_Migrable => False, Workload => 0, Period => 110, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 3, Low_Critical_Budget => 44.63558516275595, Is_Migrable => True, Workload => 0, Period => 500, CPU_Id => 2);

end E2_semi1WF_T562;
