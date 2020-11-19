with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2247 is
begin

  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 28.631093799054277, High_Critical_Budget => 57.262187598108554, Workload => 0, Period => 130, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 1, Low_Critical_Budget => 59.82081669140645, Is_Migrable => False, Workload => 0, Period => 190, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 2, Low_Critical_Budget => 3.3942411899065483, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 1);
  T_6 : High_Crit (Pri => 3, Low_Critical_Budget => 1.238232307809007, High_Critical_Budget => 2.476464615618014, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : High_Crit (Pri => 4, Low_Critical_Budget => 0.9168662941530615, High_Critical_Budget => 1.833732588306123, Workload => 0, Period => 10, CPU_Id => 2);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 0.14971283247329492, High_Critical_Budget => 0.29942566494658984, Workload => 0, Period => 500, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 8.447121475994983, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 1, Low_Critical_Budget => 22.427256982583454, Is_Migrable => True, Workload => 0, Period => 100, CPU_Id => 2);

end E4_semi1WF_T2247;
