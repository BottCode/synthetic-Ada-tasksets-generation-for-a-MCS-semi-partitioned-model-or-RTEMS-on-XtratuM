with Periodic_Tasks;

package body Taskset_E2_semi1WF_T1073 is
begin

  T_9 : High_Crit (Pri => 1, Low_Critical_Budget => 1.5986984254208159, High_Critical_Budget => 5.595444488972856, Workload => 0, Period => 10, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 0, Low_Critical_Budget => 15.19294940205067, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 2, Low_Critical_Budget => 2.0035006289037582, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 1);
  T_10 : High_Crit (Pri => 1, Low_Critical_Budget => 18.185319811023863, High_Critical_Budget => 63.64861933858352, Workload => 0, Period => 400, CPU_Id => 2);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 22.932706487700894, High_Critical_Budget => 80.26447270695313, Workload => 0, Period => 990, CPU_Id => 2);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 0.9093261376970497, High_Critical_Budget => 3.182641481939674, Workload => 0, Period => 100, CPU_Id => 2);
  T_2 : High_Crit (Pri => 5, Low_Critical_Budget => 0.0698907805823141, High_Critical_Budget => 0.24461773203809933, Workload => 0, Period => 20, CPU_Id => 2);
  T_11 : High_Crit (Pri => 4, Low_Critical_Budget => 0.05950346483219609, High_Critical_Budget => 0.2082621269126863, Workload => 0, Period => 30, CPU_Id => 2);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 47.38363759654968, Is_Migrable => False, Workload => 0, Period => 110, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 7, Low_Critical_Budget => 8.26994829165887, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 6, Low_Critical_Budget => 7.672053921874644, Is_Migrable => True, Workload => 0, Period => 110, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 8, Low_Critical_Budget => 0.440931608848838, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);

end E2_semi1WF_T1073;
