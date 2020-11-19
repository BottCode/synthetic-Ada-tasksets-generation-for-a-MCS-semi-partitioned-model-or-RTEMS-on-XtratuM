with Periodic_Tasks;

package body Taskset_E2_semi2WF_T880 is
begin

  T_5 : High_Crit (Pri => 1, Low_Critical_Budget => 31.53010834360696, High_Critical_Budget => 94.59032503082088, Workload => 0, Period => 320, CPU_Id => 1);
  T_2 : High_Crit (Pri => 2, Low_Critical_Budget => 3.373502009591396, High_Critical_Budget => 10.120506028774187, Workload => 0, Period => 70, CPU_Id => 1);
  T_10 : High_Crit (Pri => 0, Low_Critical_Budget => 10.645321898562203, High_Critical_Budget => 31.935965695686612, Workload => 0, Period => 660, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 3, Low_Critical_Budget => 12.493285199140738, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 4, Low_Critical_Budget => 2.5027444679971236, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : High_Crit (Pri => 4, Low_Critical_Budget => 0.9231470697963292, High_Critical_Budget => 2.7694412093889875, Workload => 0, Period => 10, CPU_Id => 2);
  T_0 : High_Crit (Pri => 5, Low_Critical_Budget => 0.63225109775317, High_Critical_Budget => 1.89675329325951, Workload => 0, Period => 10, CPU_Id => 2);
  T_6 : High_Crit (Pri => 0, Low_Critical_Budget => 5.589881897694124, High_Critical_Budget => 16.76964569308237, Workload => 0, Period => 410, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 2, Low_Critical_Budget => 39.85263149451444, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 2);
  T_3 : Low_Crit (Pri => 3, Low_Critical_Budget => 14.812105061263129, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 6, Low_Critical_Budget => 1.267404237543861, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 1, Low_Critical_Budget => 13.230340565359066, Is_Migrable => False, Workload => 0, Period => 520, CPU_Id => 2);

end E2_semi2WF_T880;
