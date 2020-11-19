with Taskset_E4_semi2FF_T2657;
with System;

procedure main_E4_semi2FF_T2657 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E4_semi2FF_T2657;