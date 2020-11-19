with Periodic_Tasks;

package body Taskset_E2_semi2WF_T1158 is
begin

  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 10.880705499494553, High_Critical_Budget => 40.802645623104574, Workload => 0, Period => 300, CPU_Id => 1);
  T_3 : High_Crit (Pri => 5, Low_Critical_Budget => 0.12462121293395494, High_Critical_Budget => 0.467329548502331, Workload => 0, Period => 20, CPU_Id => 1);
  T_8 : High_Crit (Pri => 3, Low_Critical_Budget => 0.05552203708416026, High_Critical_Budget => 0.20820763906560097, Workload => 0, Period => 50, CPU_Id => 1);
  T_10 : High_Crit (Pri => 2, Low_Critical_Budget => 0.07629879914713257, High_Critical_Budget => 0.2861204968017471, Workload => 0, Period => 70, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 0, Low_Critical_Budget => 340.44396580108184, Is_Migrable => False, Workload => 0, Period => 590, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.9435095681066814, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 4, Low_Critical_Budget => 18.420223024003796, Is_Migrable => False, Workload => 0, Period => 180, CPU_Id => 1);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 0.8391626263941819, High_Critical_Budget => 3.146859848978182, Workload => 0, Period => 30, CPU_Id => 2);
  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 2.5078180888322237, High_Critical_Budget => 9.404317833120839, Workload => 0, Period => 120, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 0, Low_Critical_Budget => 177.23155060380074, Is_Migrable => False, Workload => 0, Period => 400, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 4.654539258759378, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 2, Low_Critical_Budget => 19.86453857960185, Is_Migrable => False, Workload => 0, Period => 240, CPU_Id => 2);

end E2_semi2WF_T1158;
