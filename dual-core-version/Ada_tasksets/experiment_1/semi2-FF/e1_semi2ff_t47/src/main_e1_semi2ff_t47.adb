with System;
with Periodic_Tasks;

with taskset_e1_semi2ff_t47;
pragma Unreferenced (taskset_e1_semi2ff_t47);

procedure main_e1_semi2ff_t47 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
end main_e1_semi2ff_t47;