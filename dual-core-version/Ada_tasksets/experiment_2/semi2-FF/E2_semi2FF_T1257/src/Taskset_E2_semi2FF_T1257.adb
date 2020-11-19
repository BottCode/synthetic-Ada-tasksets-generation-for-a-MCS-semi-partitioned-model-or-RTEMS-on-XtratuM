with Periodic_Tasks;

package body Taskset_E2_semi2FF_T1257 is
begin

  T_2 : High_Crit (Pri => 4, Low_Critical_Budget => 2.5223981901402057, High_Critical_Budget => 10.089592760560823, Workload => 0, Period => 30, CPU_Id => 1);
  T_1 : High_Crit (Pri => 1, Low_Critical_Budget => 7.297267253070027, High_Critical_Budget => 29.189069012280108, Workload => 0, Period => 110, CPU_Id => 1);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 10.281359011433238, High_Critical_Budget => 41.125436045732954, Workload => 0, Period => 200, CPU_Id => 1);
  T_6 : High_Crit (Pri => 2, Low_Critical_Budget => 0.6837653832639636, High_Critical_Budget => 2.7350615330558545, Workload => 0, Period => 50, CPU_Id => 1);
  T_4 : High_Crit (Pri => 3, Low_Critical_Budget => 0.09780929196639421, High_Critical_Budget => 0.39123716786557683, Workload => 0, Period => 50, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 6, Low_Critical_Budget => 4.7602345392862855, Is_Migrable => True, Workload => 0, Period => 80, CPU_Id => 1);
  T_8 : Low_Crit (Pri => 7, Low_Critical_Budget => 1.5391792710724328, Is_Migrable => True, Workload => 0, Period => 50, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 5, Low_Critical_Budget => 6.004778625267941, Is_Migrable => False, Workload => 0, Period => 430, CPU_Id => 1);
  T_0 : High_Crit (Pri => 2, Low_Critical_Budget => 1.3524730611551627, High_Critical_Budget => 5.409892244620651, Workload => 0, Period => 30, CPU_Id => 2);
  T_11 : Low_Crit (Pri => 1, Low_Critical_Budget => 51.511136387231325, Is_Migrable => False, Workload => 0, Period => 130, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 3, Low_Critical_Budget => 9.858968189430698, Is_Migrable => False, Workload => 0, Period => 50, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 0, Low_Critical_Budget => 112.90330779901092, Is_Migrable => False, Workload => 0, Period => 600, CPU_Id => 2);

end E2_semi2FF_T1257;
