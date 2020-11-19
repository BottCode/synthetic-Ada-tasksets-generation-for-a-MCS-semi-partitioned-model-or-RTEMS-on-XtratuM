with Periodic_Tasks;

package body Taskset_E2_semi1WF_T962 is
begin

  T_1 : High_Crit (Pri => 4, Low_Critical_Budget => 2.8961402165308097, High_Critical_Budget => 9.412455703725131, Workload => 0, Period => 30, CPU_Id => 1);
  T_11 : High_Crit (Pri => 0, Low_Critical_Budget => 26.792820662796636, High_Critical_Budget => 87.07666715408907, Workload => 0, Period => 520, CPU_Id => 1);
  T_2 : Low_Crit (Pri => 3, Low_Critical_Budget => 39.04981794433147, Is_Migrable => False, Workload => 0, Period => 110, CPU_Id => 1);
  T_0 : Low_Crit (Pri => 5, Low_Critical_Budget => 4.40178394447154, Is_Migrable => False, Workload => 0, Period => 60, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 2.2715805539853173, Is_Migrable => False, Workload => 0, Period => 190, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 1, Low_Critical_Budget => 0.9026541871120943, Is_Migrable => False, Workload => 0, Period => 390, CPU_Id => 1);
  T_5 : High_Crit (Pri => 0, Low_Critical_Budget => 52.83965873720343, High_Critical_Budget => 171.72889089591115, Workload => 0, Period => 800, CPU_Id => 2);
  T_6 : High_Crit (Pri => 4, Low_Critical_Budget => 1.6844947080174433, High_Critical_Budget => 5.474607801056691, Workload => 0, Period => 30, CPU_Id => 2);
  T_7 : High_Crit (Pri => 2, Low_Critical_Budget => 2.3510550179047485, High_Critical_Budget => 7.6409288081904325, Workload => 0, Period => 130, CPU_Id => 2);
  T_4 : High_Crit (Pri => 3, Low_Critical_Budget => 1.518428952122919, High_Critical_Budget => 4.934894094399487, Workload => 0, Period => 90, CPU_Id => 2);
  T_9 : Low_Crit (Pri => 5, Low_Critical_Budget => 21.583849229460434, Is_Migrable => False, Workload => 0, Period => 80, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 1, Low_Critical_Budget => 102.24402557054188, Is_Migrable => True, Workload => 0, Period => 400, CPU_Id => 2);

end E2_semi1WF_T962;
