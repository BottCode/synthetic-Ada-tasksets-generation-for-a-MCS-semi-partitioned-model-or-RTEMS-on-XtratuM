with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1064 is
begin

  T_7 : High_Crit (Pri => 3, Low_Critical_Budget => 1.2931373588868738, High_Critical_Budget => 4.525980756104058, Workload => 0, Period => 30, CPU_Id => 1);
  T_0 : High_Crit (Pri => 4, Low_Critical_Budget => 0.7388604269507537, High_Critical_Budget => 2.586011494327638, Workload => 0, Period => 30, CPU_Id => 1);
  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 0.8405196715859689, High_Critical_Budget => 2.941818850550891, Workload => 0, Period => 130, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 0, Low_Critical_Budget => 346.4278600803286, Is_Migrable => False, Workload => 0, Period => 990, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 5, Low_Critical_Budget => 3.0002199671122964, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 23.921965012246638, Is_Migrable => True, Workload => 0, Period => 280, CPU_Id => 1);
  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 7.629060856906826, High_Critical_Budget => 26.701712999173893, Workload => 0, Period => 200, CPU_Id => 2);
  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 21.82258257967909, High_Critical_Budget => 76.37903902887682, Workload => 0, Period => 720, CPU_Id => 2);
  T_4 : High_Crit (Pri => 2, Low_Critical_Budget => 0.4760707131281196, High_Critical_Budget => 1.6662474959484186, Workload => 0, Period => 180, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 4, Low_Critical_Budget => 17.000784016810137, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 8.665782054648902, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.1274695162519799, Is_Migrable => True, Workload => 0, Period => 30, CPU_Id => 2);

end E2_semi1WF_T1064;
