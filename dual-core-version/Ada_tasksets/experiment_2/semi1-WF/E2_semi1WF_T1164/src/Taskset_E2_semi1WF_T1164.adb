with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1164 is
begin

  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 6.311205666138955, High_Critical_Budget => 23.66702124802108, Workload => 0, Period => 130, CPU_Id => 1);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 1.6453679828611385, High_Critical_Budget => 6.170129935729269, Workload => 0, Period => 60, CPU_Id => 1);
  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 3.558924085390224, High_Critical_Budget => 13.34596532021334, Workload => 0, Period => 180, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 3, Low_Critical_Budget => 7.884013537401051, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_7 : Low_Crit (Pri => 4, Low_Critical_Budget => 7.757840237915254, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 5, Low_Critical_Budget => 2.110997368794286, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 1);
  T_11 : High_Crit (Pri => 2, Low_Critical_Budget => 4.058000657043956, High_Critical_Budget => 15.217502463914835, Workload => 0, Period => 90, CPU_Id => 2);
  T_5 : High_Crit (Pri => 4, Low_Critical_Budget => 0.37523803480694884, High_Critical_Budget => 1.4071426305260581, Workload => 0, Period => 10, CPU_Id => 2);
  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 1.3657816234795304, High_Critical_Budget => 5.121681088048239, Workload => 0, Period => 570, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 30.11196288658127, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 1, Low_Critical_Budget => 42.07306261469335, Is_Migrable => False, Workload => 0, Period => 350, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.9032683558136145, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 2);

end E2_semi1WF_T1164;
