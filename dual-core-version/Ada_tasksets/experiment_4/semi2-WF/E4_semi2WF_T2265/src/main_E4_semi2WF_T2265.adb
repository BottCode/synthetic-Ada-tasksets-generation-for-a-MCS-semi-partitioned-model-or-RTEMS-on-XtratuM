with Taskset_E4_semi2WF_T2265;
with System;

procedure main_E4_semi2WF_T2265 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E4_semi2WF_T2265;