with Periodic_Tasks;

package body Taskset_E2_semi2FF_T550 is
begin

  T_4 : High_Crit (Pri => 1, Low_Critical_Budget => 55.61220599715323, High_Critical_Budget => 125.12746349359477, Workload => 0, Period => 460, CPU_Id => 1);
  T_2 : High_Crit (Pri => 0, Low_Critical_Budget => 92.29843027316942, High_Critical_Budget => 207.67146811463118, Workload => 0, Period => 890, CPU_Id => 1);
  T_5 : High_Crit (Pri => 2, Low_Critical_Budget => 13.742716871479148, High_Critical_Budget => 30.921112960828083, Workload => 0, Period => 140, CPU_Id => 1);
  T_8 : High_Crit (Pri => 4, Low_Critical_Budget => 2.7011759665374626, High_Critical_Budget => 6.077645924709291, Workload => 0, Period => 30, CPU_Id => 1);
  T_9 : High_Crit (Pri => 3, Low_Critical_Budget => 1.417853601526658, High_Critical_Budget => 3.190170603434981, Workload => 0, Period => 140, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.24537096861637409, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 1.4170059698633253, High_Critical_Budget => 3.188263432192482, Workload => 0, Period => 60, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 1, Low_Critical_Budget => 112.70090372615097, Is_Migrable => False, Workload => 0, Period => 440, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 0, Low_Critical_Budget => 107.61951322824305, Is_Migrable => False, Workload => 0, Period => 520, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 4, Low_Critical_Budget => 3.5579076312510596, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.2407144753621924, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 3, Low_Critical_Budget => 16.85954773695281, Is_Migrable => False, Workload => 0, Period => 180, CPU_Id => 2);

end E2_semi2FF_T550;
