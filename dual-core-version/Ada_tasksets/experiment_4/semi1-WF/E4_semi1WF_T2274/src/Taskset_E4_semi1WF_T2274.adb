with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2274 is
begin

  T_4 : High_Crit (Pri => 1, Low_Critical_Budget => 2.1879226741149003, High_Critical_Budget => 4.3758453482298005, Workload => 0, Period => 10, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 2, Low_Critical_Budget => 5.289670768951426, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 0, Low_Critical_Budget => 3.661631205928675, Is_Migrable => True, Workload => 0, Period => 30, CPU_Id => 1);
  T_7 : High_Crit (Pri => 4, Low_Critical_Budget => 1.5374688401921734, High_Critical_Budget => 3.074937680384347, Workload => 0, Period => 10, CPU_Id => 2);
  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 14.838623866604177, High_Critical_Budget => 29.677247733208354, Workload => 0, Period => 230, CPU_Id => 2);
  T_3 : High_Crit (Pri => 2, Low_Critical_Budget => 11.804105408701709, High_Critical_Budget => 23.608210817403418, Workload => 0, Period => 210, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 0, Low_Critical_Budget => 152.72474284911658, Is_Migrable => False, Workload => 0, Period => 630, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 44.088252406140484, Is_Migrable => False, Workload => 0, Period => 290, CPU_Id => 2);

end E4_semi1WF_T2274;
