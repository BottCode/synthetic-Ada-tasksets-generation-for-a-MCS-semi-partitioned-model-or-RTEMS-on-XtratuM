with Periodic_Tasks;

package body Taskset_E4_semi1WF_T2209 is
begin

  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 39.291071058450136, High_Critical_Budget => 78.58214211690027, Workload => 0, Period => 190, CPU_Id => 1);
  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 4.797087750633127, High_Critical_Budget => 9.594175501266253, Workload => 0, Period => 100, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 2, Low_Critical_Budget => 15.505286444599705, Is_Migrable => True, Workload => 0, Period => 30, CPU_Id => 1);
  T_6 : High_Crit (Pri => 1, Low_Critical_Budget => 12.117855843316539, High_Critical_Budget => 24.235711686633078, Workload => 0, Period => 80, CPU_Id => 2);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 34.854689910217004, High_Critical_Budget => 69.70937982043401, Workload => 0, Period => 320, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 2.3029944878283803, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 2, Low_Critical_Budget => 1.9587986419025594, Is_Migrable => False, Workload => 0, Period => 100, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.13447393393129836, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 2);

end E4_semi1WF_T2209;
