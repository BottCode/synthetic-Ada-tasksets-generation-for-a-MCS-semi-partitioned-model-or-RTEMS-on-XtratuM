import multiprocessing

# Set number of parallel jobs
# Watchout: in dual-core version PARALLEL_JOBS must set to 1.
PARALLEL_JOBS = 1

# Enable/disable models to check
CHECK_NO_MIGRATION = False
CHECK_SEMI_1_BF    = True
CHECK_SEMI_1_FF    = False
CHECK_SEMI_1_WF    = False
CHECK_SEMI_2_WF    = False
CHECK_SEMI_2_FF    = False
CHECK_SEMI_2_BF    = False

# Enable/disable tests to run
RUN_FIRST_TEST = False
RUN_SECOND_TEST = False
RUN_THIRD_TEST = True
RUN_FOURTH_TEST = False

# Select bin-packing algorithm to use
FIRST_FIT_BP = False
BEST_FIT_BP  = False 
WORST_FIT_BP = True

# Select version of Vestal's algorithm to use
VESTAL_CLASSIC = False
VESTAL_WITH_MONITOR = False
# Always consider HI-crit interference from HI-crit tasks
ALWAYS_HI_CRIT = True

# Number of tests to run for each Utilization step
NUMBER_OF_TESTS = 100

# Results will be saved in RESULTS_DIR
RESULTS_DIR = './results_dualcore_2/'

# The following list contains the order in which the cores enter HI-crit mode
# All the possible combinations are tested (in Model 3 a single core entering
# HI-crit mode will interfere with all the others)
CORES_MODE_CHANGES = [
  ['c1'],
  ['c2']
]

# This is the configuration used to test the NO MIGRATION model
CORES_NO_MIGRATION = {
  'c1': {'tasks': [], 'considered': False, 'utilization': 0},
  'c2': {'tasks': [], 'considered': False, 'utilization': 0}
}

# This is the configuration used to test MODEL 1
CORES_MODEL_1 = {
  'c1': {
    # List of tasks scheduled on this core
    'tasks': [],
    # Flag to determine if the core was already considered for a particular
    # task scheduling
    'considered': False,
    # Total utilization
    'utilization': 0,
    # Flag to indicate criticality change
    'crit': False,
    # Migration routes
    'migration': [
      ['c2']
    ]
  },
  'c2': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c1']
    ]
  }
}

ID_CURRENT_SYSTEM = 0

SYSTEM_MODEL = {
  'id': ID_CURRENT_SYSTEM,

  'c1': {
    # List of tasks scheduled on this core
    'tasks': [],
    # Flag to determine if the core was already considered for a particular
    # task scheduling
    'considered': False,
    # Total utilization
    'utilization': 0,
    # Flag to indicate criticality change
    'crit': False,
    # Migration routes
    'migration': [
      ['c2']
    ]
  },

  'c2': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c1']
    ]
  }

}

SYSTEMS_SCHEDULABLE_SEMI1BF = []

last_time_on_core_i = {'c1': [], 'c2': []}
last_time_on_core_i_with_additional_migrating_task = {'c1': [], 'c2': []}
where_last_mod_mig = ""