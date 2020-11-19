with Periodic_Tasks;

package body Taskset_E2_semi2WF_T1258 is
begin

  T_1 : High_Crit (Pri => 0, Low_Critical_Budget => 46.981726428298494, High_Critical_Budget => 187.92690571319397, Workload => 0, Period => 790, CPU_Id => 1);
  T_9 : High_Crit (Pri => 4, Low_Critical_Budget => 0.18860723174374455, High_Critical_Budget => 0.7544289269749782, Workload => 0, Period => 10, CPU_Id => 1);
  T_11 : High_Crit (Pri => 5, Low_Critical_Budget => 0.1620616465611716, High_Critical_Budget => 0.6482465862446865, Workload => 0, Period => 10, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 1, Low_Critical_Budget => 102.85141086496478, Is_Migrable => False, Workload => 0, Period => 340, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.462763684842734, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 3, Low_Critical_Budget => 8.354242567445233, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 2, Low_Critical_Budget => 3.0057643392435396, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 1);
  T_10 : High_Crit (Pri => 2, Low_Critical_Budget => 1.0320044088860285, High_Critical_Budget => 4.128017635544114, Workload => 0, Period => 20, CPU_Id => 2);
  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 0.6148931531007007, High_Critical_Budget => 2.459572612402803, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 1.5801486288869446, High_Critical_Budget => 6.3205945155477785, Workload => 0, Period => 450, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 1, Low_Critical_Budget => 238.80470677373395, Is_Migrable => False, Workload => 0, Period => 390, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.22079085862474201, Is_Migrable => False, Workload => 0, Period => 380, CPU_Id => 2);

end E2_semi2WF_T1258;
