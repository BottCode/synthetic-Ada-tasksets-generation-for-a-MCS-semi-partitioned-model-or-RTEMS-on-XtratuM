# Overhead parameter in order to refine RTA
# Check the following: 
#  - <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>

import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

mul = 1

overhead_values = { # in milliseconds
    # Ada runtime environment - Semi-Partitioned model on Zynq-7000
    #  - <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>

    'RTE-SPM-Zynq7000':
    {
        'DU': 0.005175*mul, # 5.175 microseconds # delay until
        'CSN': 0.000438*mul, # context switch needed
        'CSW': 0.1*mul, # context switch
        'AH': 0.002105*mul, # alarm handler
        'WEA_UA': 0.008147*mul, # Wakeup_Expired_Alarms and Update_Alarm.
        'SM': 0.001598*mul,
        'CM': 0.001018*mul,
        'BED': 0.0*mul,
        'EEV': 0.002709*mul,
        'BI': 0.11*mul,
    },
    # XtratuM according to Table 2 in
    # https://www.researchgate.net/publication/259329902_XtratuM_An_Open_Source_Hypervisor_for_TSP_Embedded_Systems_in_Aerospace
    'XtratuM':
    {
        'Save_Context': 0.005,
        'Timer_Management': 0.009,
        'Scheduler': 0.007,
        'Load_Context': 0.005,
        'Clock_Management': 0.002
    }
    # Other platforms can be added...
}

def get_runtime_metric (platform, metric):
    if platform in overhead_values.keys():
        if metric == "wakeup jitter":
            return truncate (0.00, 6) # nanoseconds precision
        elif metric == "interrupt disabled":
            return truncate (overhead_values[platform]['BI'], 6)
        elif metric == "clock handler":
            return truncate (overhead_values[platform]['AH'], 6)
        elif metric == "context switch (in)":
            return truncate (overhead_values[platform]['WEA_UA'] + overhead_values[platform]['CSN'] + overhead_values[platform]['CSW'], 6)
        elif metric == "task suspension":
            return truncate (overhead_values[platform]['DU'], 6)
        elif metric == "context switch (out)":
            return overhead_values[platform]['WEA_UA'] + overhead_values[platform]['CSW']
        elif metric == "execute expired event":
            return truncate (overhead_values[platform]['EEV'], 6)
        else:
            raise Exception ("Metric \"" + metric + "\" not supported.")
    else:
        raise Exception ("Platform \"" + platform + "\" not supported.")

def get_initial_overhead (platform): # i.e. B_i + CS1
    return get_runtime_metric (platform, "interrupt disabled") + get_runtime_metric (platform, "context switch (in)")

def get_refined_CLO (platform):
    return get_runtime_metric (platform, "context switch (in)") + get_runtime_metric (platform, "context switch (out)") + get_runtime_metric (platform, "task suspension")

def get_refined_CHI (platform):
    return get_refined_CLO (platform) + get_runtime_metric (platform, "clock handler") + get_runtime_metric (platform, "execute expired event")

def get_hypervisor_metric (platform, metric):
    if platform in overhead_values.keys():
        if metric == "Save_Context":
            return truncate (overhead_values[platform]['Save_Context'], 6) # nanoseconds precision
        elif metric == "Timer_Management":
            return truncate (overhead_values[platform]['Timer_Management'], 6)
        elif metric == "Scheduler":
            return truncate (overhead_values[platform]['Scheduler'], 6)
        elif metric == "Load_Context":
            return truncate (overhead_values[platform]['Load_Context'], 6)
        elif metric == "Clock_Management":
            return truncate (overhead_values[platform]['Clock_Management'], 6)
        else:
            raise Exception ("Metric \"" + metric + "\" not supported.")
    else:
        raise Exception ("Platform \"" + platform + "\" not supported.")

def get_partition_context_switch (platform):
    return get_hypervisor_metric (platform, "Save_Context") + get_hypervisor_metric (platform, "Timer_Management") + get_hypervisor_metric (platform, "Scheduler") + get_hypervisor_metric (platform, "Load_Context")