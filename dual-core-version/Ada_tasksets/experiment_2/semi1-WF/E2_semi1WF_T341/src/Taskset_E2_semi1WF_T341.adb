with Periodic_Tasks;

package body Taskset_E2_semi1WF_T341 is
begin

  T_4 : High_Crit (Pri => 4, Low_Critical_Budget => 2.893927412859717, High_Critical_Budget => 5.064372972504505, Workload => 0, Period => 10, CPU_Id => 1);
  T_2 : High_Crit (Pri => 0, Low_Critical_Budget => 19.57475740494329, High_Critical_Budget => 34.25582545865076, Workload => 0, Period => 320, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 0.949753424443367, High_Critical_Budget => 1.6620684927758922, Workload => 0, Period => 50, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 3, Low_Critical_Budget => 18.316698661149662, Is_Migrable => False, Workload => 0, Period => 90, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 1, Low_Critical_Budget => 16.589389175385364, Is_Migrable => False, Workload => 0, Period => 180, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.09311136520828156, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 32.23275680134894, High_Critical_Budget => 56.40732440236065, Workload => 0, Period => 140, CPU_Id => 2);
  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 24.52691044537769, High_Critical_Budget => 42.92209327941096, Workload => 0, Period => 210, CPU_Id => 2);
  T_0 : High_Crit (Pri => 3, Low_Critical_Budget => 0.3799470919074415, High_Critical_Budget => 0.6649074108380226, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 4, Low_Critical_Budget => 6.578314866516894, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 2, Low_Critical_Budget => 7.871159878187312, Is_Migrable => False, Workload => 0, Period => 150, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.3665420095571481, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);

end E2_semi1WF_T341;
