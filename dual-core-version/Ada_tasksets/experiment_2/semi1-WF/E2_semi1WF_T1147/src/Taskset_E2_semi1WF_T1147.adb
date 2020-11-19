with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1147 is
begin

  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 1.2163687377773786, High_Critical_Budget => 4.56138276666517, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : High_Crit (Pri => 0, Low_Critical_Budget => 2.9209648198282014, High_Critical_Budget => 10.953618074355756, Workload => 0, Period => 110, CPU_Id => 1);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 0.13736353092433973, High_Critical_Budget => 0.515113240966274, Workload => 0, Period => 60, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 24.19935841483479, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 4, Low_Critical_Budget => 3.7721435527153857, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 1);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 1.6363756903461837, High_Critical_Budget => 6.1364088387981885, Workload => 0, Period => 20, CPU_Id => 2);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 40.72830996359354, High_Critical_Budget => 152.73116236347576, Workload => 0, Period => 640, CPU_Id => 2);
  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 2.6496640667167384, High_Critical_Budget => 9.936240250187769, Workload => 0, Period => 420, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 5, Low_Critical_Budget => 6.886309757524431, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 2, Low_Critical_Budget => 24.36814912285181, Is_Migrable => False, Workload => 0, Period => 200, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.4332027720097162, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.8090523669026317, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);

end E2_semi1WF_T1147;
