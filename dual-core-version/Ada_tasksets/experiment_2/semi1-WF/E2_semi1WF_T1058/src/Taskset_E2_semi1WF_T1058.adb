with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1058 is
begin

  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 29.17946882430021, High_Critical_Budget => 102.12814088505073, Workload => 0, Period => 330, CPU_Id => 1);
  T_5 : High_Crit (Pri => 2, Low_Critical_Budget => 0.6185944891305072, High_Critical_Budget => 2.165080711956775, Workload => 0, Period => 20, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 13.777808950189144, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 4, Low_Critical_Budget => 6.862748021582725, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 3, Low_Critical_Budget => 8.10158905214869, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 1);
  T_0 : High_Crit (Pri => 3, Low_Critical_Budget => 0.6029877590101851, High_Critical_Budget => 2.110457156535648, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : High_Crit (Pri => 1, Low_Critical_Budget => 3.63271261528554, High_Critical_Budget => 12.71449415349939, Workload => 0, Period => 110, CPU_Id => 2);
  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 1.5235351732418907, High_Critical_Budget => 5.332373106346617, Workload => 0, Period => 90, CPU_Id => 2);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 3.101838486607744, High_Critical_Budget => 10.856434703127105, Workload => 0, Period => 510, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 6, Low_Critical_Budget => 3.332955441066978, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 5, Low_Critical_Budget => 3.531774601590074, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.31199326300282104, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);

end E2_semi1WF_T1058;
