with Taskset_E2_semi2FF_T550;
with System;

procedure main_E2_semi2FF_T550 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E2_semi2FF_T550;