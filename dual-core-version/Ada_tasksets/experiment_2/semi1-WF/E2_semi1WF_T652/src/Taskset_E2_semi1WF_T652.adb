with Periodic_Tasks;

package body Taskset_E2_semi1WF_T652 is
begin

  T_2 : High_Crit (Pri => 4, Low_Critical_Budget => 1.1689249196930023, High_Critical_Budget => 2.9223122992325057, Workload => 0, Period => 10, CPU_Id => 1);
  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 6.843439771745007, High_Critical_Budget => 17.108599429362517, Workload => 0, Period => 430, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 3, Low_Critical_Budget => 14.209214170284007, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 65.06372108928913, Is_Migrable => False, Workload => 0, Period => 300, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.6030565104051009, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 4.268786240066911, Is_Migrable => True, Workload => 0, Period => 70, CPU_Id => 1);
  T_9 : High_Crit (Pri => 2, Low_Critical_Budget => 17.781279675634483, High_Critical_Budget => 44.453199189086206, Workload => 0, Period => 310, CPU_Id => 2);
  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 12.683005137477693, High_Critical_Budget => 31.707512843694232, Workload => 0, Period => 370, CPU_Id => 2);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 24.503271625499615, High_Critical_Budget => 61.25817906374904, Workload => 0, Period => 810, CPU_Id => 2);
  T_1 : High_Crit (Pri => 3, Low_Critical_Budget => 2.4723963126631094, High_Critical_Budget => 6.180990781657774, Workload => 0, Period => 230, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 5, Low_Critical_Budget => 42.08901248541436, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 4, Low_Critical_Budget => 16.449178660652727, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 2);

end E2_semi1WF_T652;
