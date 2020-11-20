with Periodic_Tasks;

package body Taskset_E1_semi1WF_T60 is
begin

  Periodic_Tasks.Experiment_Hyperperiod :=  1_000_000;

  T_3 : High_Crit (Pri => 0, Low_Critical_Budget => 16.411023964987113, High_Critical_Budget => 32.822047929974225, Workload => 0, Period => 120, CPU_Id => 1);
  T_5 : High_Crit (Pri => 2, Low_Critical_Budget => 0.7202882849905423, High_Critical_Budget => 1.4405765699810846, Workload => 0, Period => 20, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 4, Low_Critical_Budget => 8.893617692871757, Is_Migrable => False, Workload => 0, Period => 30, CPU_Id => 1);
  T_1 : Low_Crit (Pri => 1, Low_Critical_Budget => 14.07268742508383, Is_Migrable => False, Workload => 0, Period => 70, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 3, Low_Critical_Budget => 8.467222578010363, Is_Migrable => True, Workload => 0, Period => 60, CPU_Id => 1);
  T_4 : High_Crit (Pri => 5, Low_Critical_Budget => 1.0234383530654567, High_Critical_Budget => 2.0468767061309134, Workload => 0, Period => 10, CPU_Id => 2);
  T_10 : High_Crit (Pri => 3, Low_Critical_Budget => 2.0374016142085094, High_Critical_Budget => 4.074803228417019, Workload => 0, Period => 40, CPU_Id => 2);
  T_9 : High_Crit (Pri => 4, Low_Critical_Budget => 0.23729692021447313, High_Critical_Budget => 0.47459384042894626, Workload => 0, Period => 20, CPU_Id => 2);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 0.3622327227785149, High_Critical_Budget => 0.7244654455570299, Workload => 0, Period => 60, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 86.38967758192773, Is_Migrable => False, Workload => 0, Period => 220, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 6, Low_Critical_Budget => 2.8788754141524784, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 0, Low_Critical_Budget => 59.398796411280586, Is_Migrable => False, Workload => 0, Period => 700, CPU_Id => 2);

end E1_semi1WF_T60;
