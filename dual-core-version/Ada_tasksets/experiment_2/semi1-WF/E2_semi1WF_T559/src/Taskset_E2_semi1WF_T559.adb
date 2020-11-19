with Periodic_Tasks;

package body Taskset_E2_semi1WF_T559 is
begin

  T_9 : High_Crit (Pri => 4, Low_Critical_Budget => 2.1752933293627787, High_Critical_Budget => 4.894409991066253, Workload => 0, Period => 20, CPU_Id => 1);
  T_0 : High_Crit (Pri => 1, Low_Critical_Budget => 4.599050085988203, High_Critical_Budget => 10.347862693473457, Workload => 0, Period => 120, CPU_Id => 1);
  T_11 : High_Crit (Pri => 5, Low_Critical_Budget => 0.11888886106301083, High_Critical_Budget => 0.26749993739177436, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 23.989483866930232, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 0, Low_Critical_Budget => 68.58856660485706, Is_Migrable => False, Workload => 0, Period => 340, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 2, Low_Critical_Budget => 0.9641182493139082, Is_Migrable => True, Workload => 0, Period => 70, CPU_Id => 1);
  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 4.996865291597302, High_Critical_Budget => 11.24294690609393, Workload => 0, Period => 50, CPU_Id => 2);
  T_6 : High_Crit (Pri => 1, Low_Critical_Budget => 10.921195832629405, High_Critical_Budget => 24.57269062341616, Workload => 0, Period => 200, CPU_Id => 2);
  T_3 : High_Crit (Pri => 4, Low_Critical_Budget => 0.11185345532253797, High_Critical_Budget => 0.25167027447571044, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 3, Low_Critical_Budget => 17.977319655018945, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 0, Low_Critical_Budget => 89.1357833145964, Is_Migrable => False, Workload => 0, Period => 440, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 5, Low_Critical_Budget => 5.992539103858108, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 2);

end E2_semi1WF_T559;
