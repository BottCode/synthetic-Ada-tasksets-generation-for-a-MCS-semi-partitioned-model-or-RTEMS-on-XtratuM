with Periodic_Tasks;

package body Taskset_E1_semi1WF_T56 is
begin

  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 14.554946602186163, High_Critical_Budget => 29.109893204372327, Workload => 0, Period => 100, CPU_Id => 1);
  T_3 : High_Crit (Pri => 2, Low_Critical_Budget => 1.292066444675919, High_Critical_Budget => 2.584132889351838, Workload => 0, Period => 20, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 4, Low_Critical_Budget => 6.05924335089334, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_9 : Low_Crit (Pri => 3, Low_Critical_Budget => 9.081853644981381, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 0, Low_Critical_Budget => 39.23493692905756, Is_Migrable => True, Workload => 0, Period => 310, CPU_Id => 1);
  T_0 : High_Crit (Pri => 3, Low_Critical_Budget => 6.169991836019445, High_Critical_Budget => 12.33998367203889, Workload => 0, Period => 70, CPU_Id => 2);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 35.5347772869405, High_Critical_Budget => 71.069554573881, Workload => 0, Period => 550, CPU_Id => 2);
  T_6 : High_Crit (Pri => 2, Low_Critical_Budget => 9.55696459152766, High_Critical_Budget => 19.11392918305532, Workload => 0, Period => 170, CPU_Id => 2);
  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 6.787839777770721, High_Critical_Budget => 13.575679555541441, Workload => 0, Period => 450, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.7982675863790347, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 5, Low_Critical_Budget => 5.41353313647801, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 4, Low_Critical_Budget => 8.192765280292154, Is_Migrable => False, Workload => 0, Period => 280, CPU_Id => 2);

end E1_semi1WF_T56;
