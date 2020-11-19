with Periodic_Tasks;

package body Taskset_E2_semi1WF_T848 is
begin

  T_10 : High_Crit (Pri => 4, Low_Critical_Budget => 1.023776006289408, High_Critical_Budget => 3.0713280188682237, Workload => 0, Period => 10, CPU_Id => 1);
  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 3.498742143798841, High_Critical_Budget => 10.496226431396522, Workload => 0, Period => 780, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 1, Low_Critical_Budget => 361.6185547187213, Is_Migrable => False, Workload => 0, Period => 820, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 3, Low_Critical_Budget => 9.582839748477632, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 2, Low_Critical_Budget => 20.526775274247335, Is_Migrable => True, Workload => 0, Period => 200, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 4.125579560762184, High_Critical_Budget => 12.376738682286554, Workload => 0, Period => 110, CPU_Id => 2);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 7.754320636560444, High_Critical_Budget => 23.262961909681334, Workload => 0, Period => 260, CPU_Id => 2);
  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 4.448897239986627, High_Critical_Budget => 13.34669171995988, Workload => 0, Period => 160, CPU_Id => 2);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 0.4612983255313406, High_Critical_Budget => 1.3838949765940218, Workload => 0, Period => 20, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 6, Low_Critical_Budget => 3.668004720935356, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 5, Low_Critical_Budget => 6.628707123261615, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.729679675553882, Is_Migrable => False, Workload => 0, Period => 560, CPU_Id => 2);

end E2_semi1WF_T848;
