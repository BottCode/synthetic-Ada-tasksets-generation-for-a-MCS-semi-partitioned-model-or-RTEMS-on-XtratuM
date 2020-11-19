with Periodic_Tasks;

package body Taskset_E2_semi2WF_T142 is
begin

  T_11 : High_Crit (Pri => 2, Low_Critical_Budget => 3.940688767951797, High_Critical_Budget => 4.9258609599397465, Workload => 0, Period => 10, CPU_Id => 1);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 0.1387579996257262, High_Critical_Budget => 0.17344749953215777, Workload => 0, Period => 30, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.814221297165267, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 0, Low_Critical_Budget => 86.75637084790857, Is_Migrable => False, Workload => 0, Period => 810, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 3, Low_Critical_Budget => 0.4138321311892823, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 1);
  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 49.88222792510264, High_Critical_Budget => 62.352784906378304, Workload => 0, Period => 290, CPU_Id => 2);
  T_8 : High_Crit (Pri => 6, Low_Critical_Budget => 1.2383837963368398, High_Critical_Budget => 1.5479797454210498, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : High_Crit (Pri => 4, Low_Critical_Budget => 3.1019044119383032, High_Critical_Budget => 3.877380514922879, Workload => 0, Period => 40, CPU_Id => 2);
  T_2 : High_Crit (Pri => 3, Low_Critical_Budget => 4.783335133894411, High_Critical_Budget => 5.979168917368014, Workload => 0, Period => 90, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 5, Low_Critical_Budget => 19.68450573860564, Is_Migrable => True, Workload => 0, Period => 110, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 0, Low_Critical_Budget => 99.03683640616143, Is_Migrable => False, Workload => 0, Period => 700, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 2, Low_Critical_Budget => 61.76486245923001, Is_Migrable => False, Workload => 0, Period => 660, CPU_Id => 2);

end E2_semi2WF_T142;
