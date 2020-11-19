with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1251 is
begin

  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 24.836359994938984, High_Critical_Budget => 99.34543997975594, Workload => 0, Period => 200, CPU_Id => 1);
  T_4 : High_Crit (Pri => 0, Low_Critical_Budget => 1.1135766428061022, High_Critical_Budget => 4.454306571224409, Workload => 0, Period => 490, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 3, Low_Critical_Budget => 40.570962988559494, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.0786198659007726, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 2, Low_Critical_Budget => 1.1287458611444556, Is_Migrable => False, Workload => 0, Period => 240, CPU_Id => 1);
  T_6 : High_Crit (Pri => 2, Low_Critical_Budget => 15.34179328231363, High_Critical_Budget => 61.36717312925452, Workload => 0, Period => 150, CPU_Id => 2);
  T_2 : High_Crit (Pri => 3, Low_Critical_Budget => 0.6024783760017166, High_Critical_Budget => 2.4099135040068664, Workload => 0, Period => 50, CPU_Id => 2);
  T_3 : High_Crit (Pri => 1, Low_Critical_Budget => 2.1214669403808575, High_Critical_Budget => 8.48586776152343, Workload => 0, Period => 180, CPU_Id => 2);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 0.4384509140943377, High_Critical_Budget => 1.7538036563773507, Workload => 0, Period => 290, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 4, Low_Critical_Budget => 15.146278666102297, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 5, Low_Critical_Budget => 7.538950605208827, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.9585599924821517, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 2);

end E2_semi1WF_T1251;
