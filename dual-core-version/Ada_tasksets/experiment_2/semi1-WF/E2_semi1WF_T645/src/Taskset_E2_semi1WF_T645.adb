with Periodic_Tasks;

package body Taskset_E2_semi1WF_T645 is
begin

  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 51.958024457293995, High_Critical_Budget => 129.89506114323498, Workload => 0, Period => 530, CPU_Id => 1);
  T_5 : High_Crit (Pri => 1, Low_Critical_Budget => 7.292198053475762, High_Critical_Budget => 18.230495133689406, Workload => 0, Period => 300, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 4, Low_Critical_Budget => 58.14945722066956, Is_Migrable => False, Workload => 0, Period => 120, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 3, Low_Critical_Budget => 46.22405626344217, Is_Migrable => True, Workload => 0, Period => 310, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 2, Low_Critical_Budget => 10.284294504190402, Is_Migrable => True, Workload => 0, Period => 460, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 20.696362094232676, High_Critical_Budget => 51.74090523558169, Workload => 0, Period => 400, CPU_Id => 2);
  T_4 : High_Crit (Pri => 5, Low_Critical_Budget => 0.46344286545554025, High_Critical_Budget => 1.1586071636388506, Workload => 0, Period => 10, CPU_Id => 2);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 5.659083041041109, High_Critical_Budget => 14.147707602602772, Workload => 0, Period => 240, CPU_Id => 2);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 0.6099672884092003, High_Critical_Budget => 1.5249182210230008, Workload => 0, Period => 30, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.9420687397139824, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 47.230138654819896, Is_Migrable => False, Workload => 0, Period => 260, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 4, Low_Critical_Budget => 7.837192978969856, Is_Migrable => False, Workload => 0, Period => 110, CPU_Id => 2);

end E2_semi1WF_T645;
