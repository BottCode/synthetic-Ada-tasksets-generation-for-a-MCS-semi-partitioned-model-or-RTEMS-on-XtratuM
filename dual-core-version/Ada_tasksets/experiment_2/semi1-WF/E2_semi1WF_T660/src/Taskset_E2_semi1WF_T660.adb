with Periodic_Tasks;

package body Taskset_E2_semi1WF_T660 is
begin

  T_0 : High_Crit (Pri => 1, Low_Critical_Budget => 82.38262977247521, High_Critical_Budget => 205.95657443118805, Workload => 0, Period => 440, CPU_Id => 1);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 15.719761543705568, High_Critical_Budget => 39.29940385926392, Workload => 0, Period => 580, CPU_Id => 1);
  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 2.3160747754744335, High_Critical_Budget => 5.790186938686084, Workload => 0, Period => 230, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 3, Low_Critical_Budget => 22.88708063302911, Is_Migrable => False, Workload => 0, Period => 120, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.5168869548566488, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.0929098490284006, Is_Migrable => True, Workload => 0, Period => 30, CPU_Id => 1);
  T_7 : High_Crit (Pri => 4, Low_Critical_Budget => 1.4166623718096063, High_Critical_Budget => 3.5416559295240155, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : High_Crit (Pri => 1, Low_Critical_Budget => 15.719210325971876, High_Critical_Budget => 39.29802581492969, Workload => 0, Period => 300, CPU_Id => 2);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 10.848357783436894, High_Critical_Budget => 27.120894458592236, Workload => 0, Period => 420, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 3, Low_Critical_Budget => 20.81290662628387, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 31.168299447428254, Is_Migrable => False, Workload => 0, Period => 280, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 3.300163389611006, Is_Migrable => True, Workload => 0, Period => 40, CPU_Id => 2);

end E2_semi1WF_T660;
