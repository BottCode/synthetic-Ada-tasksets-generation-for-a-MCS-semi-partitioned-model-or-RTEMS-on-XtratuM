with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1070 is
begin

  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 59.43729316108239, High_Critical_Budget => 208.03052606378836, Workload => 0, Period => 380, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 2, Low_Critical_Budget => 25.941570636553198, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 1.0770511119908477, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 1, Low_Critical_Budget => 5.436406389649999, Is_Migrable => True, Workload => 0, Period => 240, CPU_Id => 1);
  T_8 : High_Crit (Pri => 3, Low_Critical_Budget => 5.680749980751029, High_Critical_Budget => 19.8826249326286, Workload => 0, Period => 90, CPU_Id => 2);
  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 8.087199576870365, High_Critical_Budget => 28.30519851904628, Workload => 0, Period => 220, CPU_Id => 2);
  T_10 : High_Crit (Pri => 2, Low_Critical_Budget => 3.9229757532522114, High_Critical_Budget => 13.73041513638274, Workload => 0, Period => 150, CPU_Id => 2);
  T_3 : High_Crit (Pri => 4, Low_Critical_Budget => 0.4752314061508946, High_Critical_Budget => 1.663309921528131, Workload => 0, Period => 20, CPU_Id => 2);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 8.233617190941764, High_Critical_Budget => 28.817660168296175, Workload => 0, Period => 390, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 7, Low_Critical_Budget => 3.0100741724731184, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.8759566654659388, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.6381440131006109, Is_Migrable => True, Workload => 0, Period => 80, CPU_Id => 2);

end E2_semi1WF_T1070;
