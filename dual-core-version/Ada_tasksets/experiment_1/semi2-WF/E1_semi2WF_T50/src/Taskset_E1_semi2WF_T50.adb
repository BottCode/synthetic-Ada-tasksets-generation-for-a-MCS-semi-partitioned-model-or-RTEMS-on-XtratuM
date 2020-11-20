with Periodic_Tasks;

package body Taskset_E1_semi2WF_T50 is
begin

  Periodic_Tasks.Experiment_Hyperperiod :=  1_000_000;

  T_2 : High_Crit (Pri => 3, Low_Critical_Budget => 10.281701614080532, High_Critical_Budget => 20.563403228161064, Workload => 0, Period => 70, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 4.985861754443011, High_Critical_Budget => 9.971723508886022, Workload => 0, Period => 100, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 4, Low_Critical_Budget => 7.618020727190231, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 1, Low_Critical_Budget => 74.99119158664313, Is_Migrable => False, Workload => 0, Period => 360, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 0, Low_Critical_Budget => 0.9883833601224801, Is_Migrable => False, Workload => 0, Period => 550, CPU_Id => 1);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 95.35508794471633, High_Critical_Budget => 190.71017588943266, Workload => 0, Period => 780, CPU_Id => 2);
  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 18.720009169141456, High_Critical_Budget => 37.44001833828291, Workload => 0, Period => 290, CPU_Id => 2);
  T_3 : High_Crit (Pri => 1, Low_Critical_Budget => 1.5248794127404808, High_Critical_Budget => 3.0497588254809616, Workload => 0, Period => 330, CPU_Id => 2);
  T_6 : High_Crit (Pri => 3, Low_Critical_Budget => 0.7888104994172518, High_Critical_Budget => 1.5776209988345036, Workload => 0, Period => 230, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 18.314710664537046, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 4, Low_Critical_Budget => 19.781275300294585, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 6, Low_Critical_Budget => 9.560675251406682, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 2);

end E1_semi2WF_T50;
