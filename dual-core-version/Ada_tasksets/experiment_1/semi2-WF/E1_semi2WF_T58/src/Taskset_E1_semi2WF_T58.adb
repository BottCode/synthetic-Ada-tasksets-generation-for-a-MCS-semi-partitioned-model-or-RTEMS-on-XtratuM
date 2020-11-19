with Periodic_Tasks;

package body Taskset_E1_semi2WF_T58 is
begin

  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 111.53919477585231, High_Critical_Budget => 223.07838955170462, Workload => 0, Period => 530, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 4.554406600120072, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 2, Low_Critical_Budget => 5.782033719835673, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 3.0618347625855247, Is_Migrable => False, Workload => 0, Period => 150, CPU_Id => 1);
  T_8 : High_Crit (Pri => 3, Low_Critical_Budget => 13.699818077116149, High_Critical_Budget => 27.399636154232297, Workload => 0, Period => 140, CPU_Id => 2);
  T_11 : High_Crit (Pri => 4, Low_Critical_Budget => 3.163425629265348, High_Critical_Budget => 6.326851258530696, Workload => 0, Period => 60, CPU_Id => 2);
  T_7 : High_Crit (Pri => 5, Low_Critical_Budget => 1.3733365184840507, High_Critical_Budget => 2.7466730369681014, Workload => 0, Period => 60, CPU_Id => 2);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 10.556930781046125, High_Critical_Budget => 21.11386156209225, Workload => 0, Period => 550, CPU_Id => 2);
  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 6.238040136140205, High_Critical_Budget => 12.47608027228041, Workload => 0, Period => 350, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 255.48791213667218, Is_Migrable => False, Workload => 0, Period => 620, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 7, Low_Critical_Budget => 5.6627781386780445, Is_Migrable => True, Workload => 0, Period => 70, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.893127500567283, Is_Migrable => True, Workload => 0, Period => 100, CPU_Id => 2);

end E1_semi2WF_T58;
