with Taskset_E4_semi1WF_T2286;
with System;

procedure main_E4_semi1WF_T2286 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E4_semi1WF_T2286;