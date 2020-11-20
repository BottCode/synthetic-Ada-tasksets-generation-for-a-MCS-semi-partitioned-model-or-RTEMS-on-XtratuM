with Periodic_Tasks;

package body Taskset_E1_semi2WF_T63 is
begin

  Periodic_Tasks.Experiment_Hyperperiod :=  1_000_000;

  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 14.944310734119105, High_Critical_Budget => 29.88862146823821, Workload => 0, Period => 60, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 2, Low_Critical_Budget => 3.9764496684208965, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 3, Low_Critical_Budget => 0.8301365742355804, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 0, Low_Critical_Budget => 30.759139518661893, Is_Migrable => False, Workload => 0, Period => 720, CPU_Id => 1);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 26.283242661784342, High_Critical_Budget => 52.566485323568685, Workload => 0, Period => 420, CPU_Id => 2);
  T_8 : High_Crit (Pri => 2, Low_Critical_Budget => 7.4166147284748725, High_Critical_Budget => 14.833229456949745, Workload => 0, Period => 120, CPU_Id => 2);
  T_4 : High_Crit (Pri => 5, Low_Critical_Budget => 0.23867709315299135, High_Critical_Budget => 0.4773541863059827, Workload => 0, Period => 10, CPU_Id => 2);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 17.006151177241104, High_Critical_Budget => 34.01230235448221, Workload => 0, Period => 840, CPU_Id => 2);
  T_0 : High_Crit (Pri => 6, Low_Critical_Budget => 0.000991267235359583, High_Critical_Budget => 0.001982534470719166, Workload => 0, Period => 10, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 4, Low_Critical_Budget => 53.11955983507043, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 3, Low_Critical_Budget => 22.73584839682838, Is_Migrable => False, Workload => 0, Period => 190, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 7, Low_Critical_Budget => 3.400369867807571, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);

end E1_semi2WF_T63;
