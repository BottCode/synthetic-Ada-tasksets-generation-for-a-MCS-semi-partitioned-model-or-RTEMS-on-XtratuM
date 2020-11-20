with System;
with Periodic_Tasks;

with taskset_e1_semi2wf_t59;
pragma Unreferenced (taskset_e1_semi2wf_t59);

procedure main_e1_semi2wf_t59 is
    pragma Priority (System.Priority'Last);
    pragma CPU (1);
begin
    Periodic_Tasks.Init;
end main_e1_semi2wf_t59;