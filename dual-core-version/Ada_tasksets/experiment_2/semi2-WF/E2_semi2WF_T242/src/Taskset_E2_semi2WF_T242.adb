with Periodic_Tasks;

package body Taskset_E2_semi2WF_T242 is
begin

  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 24.82372482141774, High_Critical_Budget => 37.23558723212661, Workload => 0, Period => 80, CPU_Id => 1);
  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 18.342087388761286, High_Critical_Budget => 27.51313108314193, Workload => 0, Period => 320, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 0, Low_Critical_Budget => 125.36886098098682, Is_Migrable => False, Workload => 0, Period => 580, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 3, Low_Critical_Budget => 28.90478313724316, Is_Migrable => False, Workload => 0, Period => 150, CPU_Id => 1);
  T_9 : High_Crit (Pri => 2, Low_Critical_Budget => 30.3713952240166, High_Critical_Budget => 45.5570928360249, Workload => 0, Period => 230, CPU_Id => 2);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 69.0498426590572, High_Critical_Budget => 103.5747639885858, Workload => 0, Period => 690, CPU_Id => 2);
  T_0 : High_Crit (Pri => 1, Low_Critical_Budget => 35.30344569581292, High_Critical_Budget => 52.95516854371938, Workload => 0, Period => 450, CPU_Id => 2);
  T_6 : High_Crit (Pri => 5, Low_Critical_Budget => 0.0781174882442226, High_Critical_Budget => 0.1171762323663339, Workload => 0, Period => 30, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 4, Low_Critical_Budget => 124.8560119319746, Is_Migrable => False, Workload => 0, Period => 530, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 7, Low_Critical_Budget => 3.169600347996502, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 3, Low_Critical_Budget => 6.576754787349586, Is_Migrable => False, Workload => 0, Period => 670, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.36508288714993675, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 2);

end E2_semi2WF_T242;
