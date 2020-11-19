with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2561 is
begin

  T_2 : High_Crit (Pri => 6, Low_Critical_Budget => 1.8259758086345312, High_Critical_Budget => 3.6519516172690625, Workload => 0, Period => 10, CPU_Id => 1);
  T_6 : High_Crit (Pri => 3, Low_Critical_Budget => 3.7628387265417373, High_Critical_Budget => 7.525677453083475, Workload => 0, Period => 40, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 6.3279164055456425, High_Critical_Budget => 12.655832811091285, Workload => 0, Period => 370, CPU_Id => 1);
  T_0 : High_Crit (Pri => 4, Low_Critical_Budget => 0.2901978538904437, High_Critical_Budget => 0.5803957077808874, Workload => 0, Period => 20, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 7, Low_Critical_Budget => 1.4292854070692562, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 2, Low_Critical_Budget => 19.49323023056106, Is_Migrable => False, Workload => 0, Period => 180, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 1, Low_Critical_Budget => 25.053430793363546, Is_Migrable => False, Workload => 0, Period => 340, CPU_Id => 1);
  T_14 : Low_Crit (Pri => 5, Low_Critical_Budget => 7.727185377832566, Is_Migrable => True, Workload => 0, Period => 120, CPU_Id => 1);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 82.62170219242186, High_Critical_Budget => 165.24340438484373, Workload => 0, Period => 590, CPU_Id => 2);
  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 36.276156701235024, High_Critical_Budget => 72.55231340247005, Workload => 0, Period => 330, CPU_Id => 2);
  T_8 : High_Crit (Pri => 2, Low_Critical_Budget => 6.377286385822415, High_Critical_Budget => 12.75457277164483, Workload => 0, Period => 170, CPU_Id => 2);
  T_12 : High_Crit (Pri => 3, Low_Critical_Budget => 1.5725490274437994, High_Critical_Budget => 3.145098054887599, Workload => 0, Period => 100, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.0898234467978867, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_13 : Low_Crit (Pri => 4, Low_Critical_Budget => 7.198557666987901, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.35908302266342007, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);

end E4_semi1WF_T2561;
