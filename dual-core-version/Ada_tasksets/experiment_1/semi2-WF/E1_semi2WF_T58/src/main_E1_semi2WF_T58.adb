with Taskset_E1_semi2WF_T58;
with System;

procedure main_E1_semi2WF_T58 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E1_semi2WF_T58;