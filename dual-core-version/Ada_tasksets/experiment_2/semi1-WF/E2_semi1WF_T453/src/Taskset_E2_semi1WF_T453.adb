with Periodic_Tasks;

package body Taskset_E2_semi1WF_T453 is
begin

  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 7.977159510482816, High_Critical_Budget => 15.954319020965633, Workload => 0, Period => 60, CPU_Id => 1);
  T_5 : High_Crit (Pri => 3, Low_Critical_Budget => 1.1560467004924524, High_Critical_Budget => 2.312093400984905, Workload => 0, Period => 30, CPU_Id => 1);
  T_1 : High_Crit (Pri => 4, Low_Critical_Budget => 0.5251407806353536, High_Critical_Budget => 1.0502815612707073, Workload => 0, Period => 20, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 0, Low_Critical_Budget => 131.0386721094777, Is_Migrable => False, Workload => 0, Period => 440, CPU_Id => 1);
  T_9 : Low_Crit (Pri => 1, Low_Critical_Budget => 73.58728940392398, Is_Migrable => False, Workload => 0, Period => 370, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.4186272667472646, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_8 : High_Crit (Pri => 3, Low_Critical_Budget => 2.508250891396193, High_Critical_Budget => 5.016501782792386, Workload => 0, Period => 20, CPU_Id => 2);
  T_2 : High_Crit (Pri => 1, Low_Critical_Budget => 2.548261415301729, High_Critical_Budget => 5.096522830603458, Workload => 0, Period => 40, CPU_Id => 2);
  T_4 : High_Crit (Pri => 2, Low_Critical_Budget => 0.7211048479071236, High_Critical_Budget => 1.4422096958142472, Workload => 0, Period => 30, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 0, Low_Critical_Budget => 172.900301885876, Is_Migrable => False, Workload => 0, Period => 620, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 4, Low_Critical_Budget => 1.9572978576083677, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.7703531152376386, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);

end E2_semi1WF_T453;
