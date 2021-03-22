# Overhead parameter in order to refine RTA
# Check the following: 
#  - <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>

import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

overhead_values = { # in milliseconds
    # Ada runtime environment - Semi-Partitioned model on Zynq-7000
    'RTE-SPM-Zynq7000':
    {
        'DU': 0.005175, # 5.175 microseconds
        'CSN': 0.000438,
        'CSW': 0.1,
        'AH': 0.002105,
        'WEA_UA': 0.008147,
        'SM': 0.001598,
        'CM': 0.001018,
        'BED': 0.0,
        'EEV': 0.002709,
        'BI': 0.11,
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