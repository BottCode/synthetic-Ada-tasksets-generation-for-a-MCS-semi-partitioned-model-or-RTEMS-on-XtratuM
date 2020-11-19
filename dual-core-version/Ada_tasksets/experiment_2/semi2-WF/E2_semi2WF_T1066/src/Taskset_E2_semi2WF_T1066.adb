with Periodic_Tasks;

package body Taskset_E2_semi2WF_T1066 is
begin

  T_5 : High_Crit (Pri => 1, Low_Critical_Budget => 20.409754010152845, High_Critical_Budget => 71.43413903553495, Workload => 0, Period => 240, CPU_Id => 1);
  T_2 : High_Crit (Pri => 4, Low_Critical_Budget => 0.48740678329080467, High_Critical_Budget => 1.7059237415178163, Workload => 0, Period => 20, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 13.639600977046383, High_Critical_Budget => 47.73860341966234, Workload => 0, Period => 980, CPU_Id => 1);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 0.9810491213128805, High_Critical_Budget => 3.4336719245950817, Workload => 0, Period => 90, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.5039044749260713, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 5, Low_Critical_Budget => 3.645734275916106, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 3, Low_Critical_Budget => 17.57350143759451, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 1);
  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 31.184601216305925, High_Critical_Budget => 109.14610425707073, Workload => 0, Period => 390, CPU_Id => 2);
  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 24.748002567888484, High_Critical_Budget => 86.6180089876097, Workload => 0, Period => 570, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 2.8206440179184056, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 1.9089460090394295, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.010023926131166316, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);

end E2_semi2WF_T1066;
