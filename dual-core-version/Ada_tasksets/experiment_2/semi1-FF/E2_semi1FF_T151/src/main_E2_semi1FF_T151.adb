with Taskset_E2_semi1FF_T151;
with System;

procedure main_E2_semi1FF_T151 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
endmain_E2_semi1FF_T151;