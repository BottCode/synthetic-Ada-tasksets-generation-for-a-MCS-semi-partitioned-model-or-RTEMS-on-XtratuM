with Taskset_E2_semi1WF_T1058;
with System;

procedure main_E2_semi1WF_T1058 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E2_semi1WF_T1058;