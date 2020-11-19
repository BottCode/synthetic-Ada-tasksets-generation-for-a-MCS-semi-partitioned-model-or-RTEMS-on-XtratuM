with Periodic_Tasks;

package body Taskset_E2_semi2WF_T945 is
begin

  T_4 : High_Crit (Pri => 0, Low_Critical_Budget => 26.28040086769122, High_Critical_Budget => 85.41130281999646, Workload => 0, Period => 300, CPU_Id => 1);
  T_5 : High_Crit (Pri => 2, Low_Critical_Budget => 6.78254092888532, High_Critical_Budget => 22.04325801887729, Workload => 0, Period => 150, CPU_Id => 1);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 6.873420626077564, High_Critical_Budget => 22.338617034752083, Workload => 0, Period => 300, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 3, Low_Critical_Budget => 25.938784489268023, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.6041938808489054, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 7.4628547555852975, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 1);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 1.5167606063681647, High_Critical_Budget => 4.929471970696535, Workload => 0, Period => 20, CPU_Id => 2);
  T_6 : High_Crit (Pri => 1, Low_Critical_Budget => 14.43871947542763, High_Critical_Budget => 46.9258382951398, Workload => 0, Period => 230, CPU_Id => 2);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 1.9775124485968407, High_Critical_Budget => 6.4269154579397325, Workload => 0, Period => 330, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 5.599134062310207, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 4, Low_Critical_Budget => 4.149410148996126, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 3, Low_Critical_Budget => 0.2458382501572931, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 2);

end E2_semi2WF_T945;
