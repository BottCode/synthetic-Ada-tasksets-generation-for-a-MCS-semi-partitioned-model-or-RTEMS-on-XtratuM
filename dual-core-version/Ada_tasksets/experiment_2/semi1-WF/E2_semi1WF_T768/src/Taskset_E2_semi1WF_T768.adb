with Periodic_Tasks;

package body Taskset_E2_semi1WF_T768 is
begin

  T_4 : High_Crit (Pri => 0, Low_Critical_Budget => 100.30121241084125, High_Critical_Budget => 275.8283341298134, Workload => 0, Period => 970, CPU_Id => 1);
  T_2 : High_Crit (Pri => 3, Low_Critical_Budget => 0.08351154736962453, High_Critical_Budget => 0.22965675526646745, Workload => 0, Period => 10, CPU_Id => 1);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 1.0322767526538954, High_Critical_Budget => 2.8387610697982124, Workload => 0, Period => 160, CPU_Id => 1);
  T_3 : High_Crit (Pri => 4, Low_Critical_Budget => 0.04238040062947832, High_Critical_Budget => 0.11654610173106539, Workload => 0, Period => 10, CPU_Id => 1);
  T_9 : Low_Crit (Pri => 6, Low_Critical_Budget => 3.7869237307974304, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 4.156765384955525, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 2, Low_Critical_Budget => 6.184535852729194, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 1);
  T_6 : High_Crit (Pri => 3, Low_Critical_Budget => 1.7994676644797933, High_Critical_Budget => 4.948536077319432, Workload => 0, Period => 20, CPU_Id => 2);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 42.796250840391004, High_Critical_Budget => 117.68968981107527, Workload => 0, Period => 640, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 2, Low_Critical_Budget => 20.874354281217794, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 1, Low_Critical_Budget => 12.64487087684536, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.9835908525464798, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);

end E2_semi1WF_T768;
