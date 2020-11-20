with Taskset_E1_semi1WF_T63;
with System;

procedure main_E1_semi1WF_T63 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
end main_E1_semi1WF_T63;