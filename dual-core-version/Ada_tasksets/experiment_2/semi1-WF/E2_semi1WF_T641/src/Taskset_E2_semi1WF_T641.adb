with Periodic_Tasks;

package body Taskset_E2_semi1WF_T641 is
begin

  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 2.053144606692783, High_Critical_Budget => 5.132861516731958, Workload => 0, Period => 30, CPU_Id => 1);
  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 0.6322792908638197, High_Critical_Budget => 1.5806982271595493, Workload => 0, Period => 20, CPU_Id => 1);
  T_9 : High_Crit (Pri => 2, Low_Critical_Budget => 0.1413647328069667, High_Critical_Budget => 0.35341183201741677, Workload => 0, Period => 10, CPU_Id => 1);
  T_8 : High_Crit (Pri => 3, Low_Critical_Budget => 0.07611319709503972, High_Critical_Budget => 0.1902829927375993, Workload => 0, Period => 10, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 5, Low_Critical_Budget => 3.1513175338125166, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.226306017091595, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_5 : Low_Crit (Pri => 4, Low_Critical_Budget => 0.13145484905941585, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 11.268168050350777, High_Critical_Budget => 28.17042012587694, Workload => 0, Period => 170, CPU_Id => 2);
  T_1 : High_Crit (Pri => 3, Low_Critical_Budget => 1.8919899236553448, High_Critical_Budget => 4.729974809138362, Workload => 0, Period => 30, CPU_Id => 2);
  T_10 : Low_Crit (Pri => 0, Low_Critical_Budget => 183.2475162923371, Is_Migrable => False, Workload => 0, Period => 770, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.3057869644764053, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 35.86112284299841, Is_Migrable => True, Workload => 0, Period => 180, CPU_Id => 2);

end E2_semi1WF_T641;
