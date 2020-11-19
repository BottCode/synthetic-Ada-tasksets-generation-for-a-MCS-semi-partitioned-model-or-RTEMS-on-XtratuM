with Periodic_Tasks;

package body Taskset_E2_semi1WF_T655 is
begin

  T_1 : High_Crit (Pri => 0, Low_Critical_Budget => 91.06306422479611, High_Critical_Budget => 227.65766056199027, Workload => 0, Period => 770, CPU_Id => 1);
  T_3 : High_Crit (Pri => 1, Low_Critical_Budget => 9.61433782648486, High_Critical_Budget => 24.03584456621215, Workload => 0, Period => 450, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 4, Low_Critical_Budget => 9.93304396898418, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 3, Low_Critical_Budget => 15.051317694129489, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 2, Low_Critical_Budget => 15.656148738976265, Is_Migrable => True, Workload => 0, Period => 140, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 36.35864136451648, High_Critical_Budget => 90.8966034112912, Workload => 0, Period => 800, CPU_Id => 2);
  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 5.176054168120874, High_Critical_Budget => 12.940135420302186, Workload => 0, Period => 120, CPU_Id => 2);
  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 22.085805984813945, High_Critical_Budget => 55.21451496203486, Workload => 0, Period => 670, CPU_Id => 2);
  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 0.4852988131801501, High_Critical_Budget => 1.2132470329503753, Workload => 0, Period => 30, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 5, Low_Critical_Budget => 11.31496873328696, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.6997960256542144, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 4, Low_Critical_Budget => 6.28840887449309, Is_Migrable => False, Workload => 0, Period => 120, CPU_Id => 2);

end E2_semi1WF_T655;
