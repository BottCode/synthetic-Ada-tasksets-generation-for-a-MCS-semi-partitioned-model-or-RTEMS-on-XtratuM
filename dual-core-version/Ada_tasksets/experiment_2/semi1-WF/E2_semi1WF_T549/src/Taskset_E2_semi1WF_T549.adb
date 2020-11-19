with Periodic_Tasks;

package body Taskset_E2_semi1WF_T549 is
begin

  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 110.57653025740059, High_Critical_Budget => 248.79719307915133, Workload => 0, Period => 760, CPU_Id => 1);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 9.829112024859814, High_Critical_Budget => 22.11550205593458, Workload => 0, Period => 130, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 4, Low_Critical_Budget => 14.789855126415386, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 77.10879223869215, Is_Migrable => True, Workload => 0, Period => 440, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 3, Low_Critical_Budget => 1.7056973898196959, Is_Migrable => True, Workload => 0, Period => 130, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 8.058273735255042, High_Critical_Budget => 18.131115904323845, Workload => 0, Period => 90, CPU_Id => 2);
  T_10 : High_Crit (Pri => 2, Low_Critical_Budget => 4.6132344720375364, High_Critical_Budget => 10.379777562084456, Workload => 0, Period => 60, CPU_Id => 2);
  T_4 : High_Crit (Pri => 3, Low_Critical_Budget => 0.35038665668185687, High_Critical_Budget => 0.7883699775341779, Workload => 0, Period => 10, CPU_Id => 2);
  T_11 : High_Crit (Pri => 1, Low_Critical_Budget => 0.6517143880282267, High_Critical_Budget => 1.46635737306351, Workload => 0, Period => 70, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 6, Low_Critical_Budget => 3.339583774804389, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 2);
  T_0 : Low_Crit (Pri => 4, Low_Critical_Budget => 4.384726776014998, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 5, Low_Critical_Budget => 1.420619647176462, Is_Migrable => True, Workload => 0, Period => 40, CPU_Id => 2);

end E2_semi1WF_T549;
