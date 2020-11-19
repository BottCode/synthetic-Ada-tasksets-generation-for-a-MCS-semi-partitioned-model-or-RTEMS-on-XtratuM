with Taskset_E4_semi1FF_T2357;
with System;

procedure main_E4_semi1FF_T2357 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E4_semi1FF_T2357;