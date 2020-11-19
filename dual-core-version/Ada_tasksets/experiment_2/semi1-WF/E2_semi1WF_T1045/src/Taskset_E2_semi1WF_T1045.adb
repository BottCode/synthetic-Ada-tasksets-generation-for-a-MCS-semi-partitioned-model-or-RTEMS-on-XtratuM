with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1045 is
begin

  T_0 : High_Crit (Pri => 0, Low_Critical_Budget => 30.46385058959956, High_Critical_Budget => 106.62347706359846, Workload => 0, Period => 290, CPU_Id => 1);
  T_2 : High_Crit (Pri => 4, Low_Critical_Budget => 0.15039376610144523, High_Critical_Budget => 0.5263781813550583, Workload => 0, Period => 10, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 2, Low_Critical_Budget => 25.48424340674447, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 15.427747157757528, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 1, Low_Critical_Budget => 8.129565344413848, Is_Migrable => True, Workload => 0, Period => 150, CPU_Id => 1);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 33.185739319513765, High_Critical_Budget => 116.15008761829817, Workload => 0, Period => 630, CPU_Id => 2);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 13.08508121736528, High_Critical_Budget => 45.79778426077848, Workload => 0, Period => 350, CPU_Id => 2);
  T_6 : High_Crit (Pri => 1, Low_Critical_Budget => 8.503628566051729, High_Critical_Budget => 29.762699981181054, Workload => 0, Period => 530, CPU_Id => 2);
  T_3 : High_Crit (Pri => 3, Low_Critical_Budget => 0.8988137710415067, High_Critical_Budget => 3.1458481986452735, Workload => 0, Period => 150, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 77.5144890175966, Is_Migrable => False, Workload => 0, Period => 260, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 6, Low_Critical_Budget => 5.136408418295202, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 4, Low_Critical_Budget => 28.748798960717775, Is_Migrable => False, Workload => 0, Period => 310, CPU_Id => 2);

end E2_semi1WF_T1045;
