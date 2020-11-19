with Periodic_Tasks;

package body Taskset_E2_semi1WF_T546 is
begin

  T_9 : High_Crit (Pri => 2, Low_Critical_Budget => 3.848427234851623, High_Critical_Budget => 8.658961278416152, Workload => 0, Period => 30, CPU_Id => 1);
  T_8 : High_Crit (Pri => 0, Low_Critical_Budget => 1.2333673438609634, High_Critical_Budget => 2.7750765236871677, Workload => 0, Period => 60, CPU_Id => 1);
  T_11 : High_Crit (Pri => 3, Low_Critical_Budget => 0.3686815787584442, High_Critical_Budget => 0.8295335522064995, Workload => 0, Period => 20, CPU_Id => 1);
  T_0 : High_Crit (Pri => 4, Low_Critical_Budget => 0.16304762850012958, High_Critical_Budget => 0.36685716412529157, Workload => 0, Period => 10, CPU_Id => 1);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 27.463539957052983, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 1);
  T_4 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.12564736655505504, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 7, Low_Critical_Budget => 0.07798270462364254, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.1517341289507046, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_10 : High_Crit (Pri => 3, Low_Critical_Budget => 3.3623319938832656, High_Critical_Budget => 7.565246986237348, Workload => 0, Period => 30, CPU_Id => 2);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 3.781148349299055, High_Critical_Budget => 8.507583785922874, Workload => 0, Period => 50, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 0, Low_Critical_Budget => 266.9824649318216, Is_Migrable => False, Workload => 0, Period => 750, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 1, Low_Critical_Budget => 99.0971280402033, Is_Migrable => True, Workload => 0, Period => 530, CPU_Id => 2);

end E2_semi1WF_T546;
