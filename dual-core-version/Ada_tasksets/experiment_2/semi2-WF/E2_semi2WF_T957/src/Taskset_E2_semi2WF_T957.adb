with Periodic_Tasks;

package body Taskset_E2_semi2WF_T957 is
begin

  T_1 : High_Crit (Pri => 0, Low_Critical_Budget => 32.762925923762126, High_Critical_Budget => 106.4795092522269, Workload => 0, Period => 240, CPU_Id => 1);
  T_11 : High_Crit (Pri => 4, Low_Critical_Budget => 0.09750006268813668, High_Critical_Budget => 0.31687520373644423, Workload => 0, Period => 10, CPU_Id => 1);
  T_3 : High_Crit (Pri => 1, Low_Critical_Budget => 1.4636339846649518, High_Critical_Budget => 4.756810450161093, Workload => 0, Period => 220, CPU_Id => 1);
  T_7 : High_Crit (Pri => 3, Low_Critical_Budget => 0.06443562999464802, High_Critical_Budget => 0.20941579748260608, Workload => 0, Period => 20, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 2, Low_Critical_Budget => 45.48920021557159, Is_Migrable => False, Workload => 0, Period => 160, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.4601213424085566, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.6794416416746718, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_4 : High_Crit (Pri => 2, Low_Critical_Budget => 1.7112671706935245, High_Critical_Budget => 5.561618304753955, Workload => 0, Period => 20, CPU_Id => 2);
  T_5 : High_Crit (Pri => 1, Low_Critical_Budget => 2.539786178868918, High_Critical_Budget => 8.254305081323984, Workload => 0, Period => 30, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.6087765867462394, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 0, Low_Critical_Budget => 53.24622820050172, Is_Migrable => False, Workload => 0, Period => 470, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 3, Low_Critical_Budget => 0.7771663707584342, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);

end E2_semi2WF_T957;
