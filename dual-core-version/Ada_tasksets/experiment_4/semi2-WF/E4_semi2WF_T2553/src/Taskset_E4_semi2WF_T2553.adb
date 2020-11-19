with Periodic_Tasks;

package body Taskset_E4_semi2WF_T2553 is
begin

  T_7 : High_Crit (Pri => 1, Low_Critical_Budget => 15.421638267948596, High_Critical_Budget => 30.843276535897193, Workload => 0, Period => 160, CPU_Id => 1);
  T_5 : High_Crit (Pri => 4, Low_Critical_Budget => 0.5790356649500694, High_Critical_Budget => 1.1580713299001388, Workload => 0, Period => 10, CPU_Id => 1);
  T_4 : High_Crit (Pri => 3, Low_Critical_Budget => 0.6310337412267542, High_Critical_Budget => 1.2620674824535083, Workload => 0, Period => 40, CPU_Id => 1);
  T_9 : High_Crit (Pri => 0, Low_Critical_Budget => 4.910803484383958, High_Critical_Budget => 9.821606968767917, Workload => 0, Period => 510, CPU_Id => 1);
  T_10 : High_Crit (Pri => 2, Low_Critical_Budget => 0.262336000444765, High_Critical_Budget => 0.52467200088953, Workload => 0, Period => 110, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 6, Low_Critical_Budget => 6.255245271820637, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_14 : Low_Crit (Pri => 7, Low_Critical_Budget => 0.07552724590609339, Is_Migrable => False, Workload => 0, Period => 10, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.009863694152931757, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_13 : High_Crit (Pri => 0, Low_Critical_Budget => 72.01557747887486, High_Critical_Budget => 144.03115495774972, Workload => 0, Period => 840, CPU_Id => 2);
  T_3 : High_Crit (Pri => 3, Low_Critical_Budget => 2.677087071062183, High_Critical_Budget => 5.354174142124366, Workload => 0, Period => 40, CPU_Id => 2);
  T_8 : High_Crit (Pri => 2, Low_Critical_Budget => 3.7846904875552534, High_Critical_Budget => 7.569380975110507, Workload => 0, Period => 80, CPU_Id => 2);
  T_6 : Low_Crit (Pri => 1, Low_Critical_Budget => 199.22594946758815, Is_Migrable => False, Workload => 0, Period => 540, CPU_Id => 2);
  T_2 : Low_Crit (Pri => 5, Low_Critical_Budget => 0.6132825566361877, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);
  T_12 : Low_Crit (Pri => 4, Low_Critical_Budget => 17.83831966151734, Is_Migrable => False, Workload => 0, Period => 360, CPU_Id => 2);
  T_1 : Low_Crit (Pri => 6, Low_Critical_Budget => 0.3451910329964969, Is_Migrable => True, Workload => 0, Period => 10, CPU_Id => 2);

end E4_semi2WF_T2553;
