with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1244 is
begin

  T_7 : High_Crit (Pri => 3, Low_Critical_Budget => 4.526693028881744, High_Critical_Budget => 18.106772115526976, Workload => 0, Period => 90, CPU_Id => 1);
  T_11 : High_Crit (Pri => 2, Low_Critical_Budget => 3.05421966732219, High_Critical_Budget => 12.21687866928876, Workload => 0, Period => 120, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 12.140300921760467, High_Critical_Budget => 48.56120368704187, Workload => 0, Period => 500, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 5, Low_Critical_Budget => 41.338447964693074, Is_Migrable => False, Workload => 0, Period => 120, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 1, Low_Critical_Budget => 47.33606049192301, Is_Migrable => False, Workload => 0, Period => 400, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 4, Low_Critical_Budget => 20.288358700346883, Is_Migrable => True, Workload => 0, Period => 180, CPU_Id => 1);
  T_10 : High_Crit (Pri => 3, Low_Critical_Budget => 0.8851160791368212, High_Critical_Budget => 3.540464316547285, Workload => 0, Period => 20, CPU_Id => 2);
  T_3 : High_Crit (Pri => 4, Low_Critical_Budget => 0.31719509963971826, High_Critical_Budget => 1.268780398558873, Workload => 0, Period => 10, CPU_Id => 2);
  T_2 : High_Crit (Pri => 0, Low_Critical_Budget => 2.111948607021827, High_Critical_Budget => 8.447794428087308, Workload => 0, Period => 350, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 110.32467880167181, Is_Migrable => False, Workload => 0, Period => 230, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 5.205122532505424, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 1, Low_Critical_Budget => 8.788480671830918, Is_Migrable => False, Workload => 0, Period => 530, CPU_Id => 2);

end E2_semi1WF_T1244;
