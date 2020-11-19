with Periodic_Tasks;

package body Taskset_E2_semi2WF_T867 is
begin

  T_2 : High_Crit (Pri => 0, Low_Critical_Budget => 19.203033458977636, High_Critical_Budget => 57.60910037693291, Workload => 0, Period => 150, CPU_Id => 1);
  T_10 : Low_Crit (Pri => 1, Low_Critical_Budget => 10.474314870438226, Is_Migrable => False, Workload => 0, Period => 20, CPU_Id => 1);
  T_3 : Low_Crit (Pri => 2, Low_Critical_Budget => 1.5687101422696603, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 1);
  T_11 : Low_Crit (Pri => 3, Low_Critical_Budget => 1.4409206763442413, Is_Migrable => True, Workload => 0, Period => 20, CPU_Id => 1);
  T_6 : High_Crit (Pri => 1, Low_Critical_Budget => 10.539868239845296, High_Critical_Budget => 31.619604719535886, Workload => 0, Period => 200, CPU_Id => 2);
  T_9 : High_Crit (Pri => 5, Low_Critical_Budget => 0.3156930765119185, High_Critical_Budget => 0.9470792295357555, Workload => 0, Period => 10, CPU_Id => 2);
  T_4 : High_Crit (Pri => 3, Low_Critical_Budget => 1.3602239008850558, High_Critical_Budget => 4.0806717026551675, Workload => 0, Period => 60, CPU_Id => 2);
  T_0 : High_Crit (Pri => 6, Low_Critical_Budget => 0.20644562470753267, High_Critical_Budget => 0.619336874122598, Workload => 0, Period => 10, CPU_Id => 2);
  T_1 : High_Crit (Pri => 2, Low_Critical_Budget => 0.8237836305196433, High_Critical_Budget => 2.47135089155893, Workload => 0, Period => 180, CPU_Id => 2);
  T_5 : Low_Crit (Pri => 0, Low_Critical_Budget => 192.13282180803108, Is_Migrable => False, Workload => 0, Period => 480, CPU_Id => 2);
  T_7 : Low_Crit (Pri => 7, Low_Critical_Budget => 5.0368121685350475, Is_Migrable => False, Workload => 0, Period => 40, CPU_Id => 2);
  T_8 : Low_Crit (Pri => 4, Low_Critical_Budget => 5.121921116243831, Is_Migrable => False, Workload => 0, Period => 340, CPU_Id => 2);

end E2_semi2WF_T867;
