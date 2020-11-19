with Taskset_E1_semi1WF_T56;
with System;

procedure main_E1_semi1WF_T56 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E1_semi1WF_T56;