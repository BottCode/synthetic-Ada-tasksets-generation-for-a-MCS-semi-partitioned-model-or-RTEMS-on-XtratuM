import multiprocessing

# Set number of parallel jobs
PARALLEL_JOBS = multiprocessing.cpu_count()

# Enable/disable models to check
CHECK_NO_MIGRATION = True
CHECK_MODEL_1 = True
CHECK_MODEL_2 = False
CHECK_MODEL_3 = False

# Enable/disable tests to run
RUN_FIRST_TEST =  True
RUN_SECOND_TEST = False
RUN_THIRD_TEST = False
RUN_FOURTH_TEST = False

# Select bin-packing algorithm to use
FIRST_FIT_BP = True
WORST_FIT_BP = False

# Select version of Vestal's algorithm to use
VESTAL_CLASSIC = False
VESTAL_WITH_MONITOR = False
# Always consider HI-crit interference from HI-crit tasks
ALWAYS_HI_CRIT = True

# Number of tests to run for each Utilization step
NUMBER_OF_TESTS = 5

# Results will be saved in RESULTS_DIR
RESULTS_DIR = './results/'

# The following list contains the order in which the cores enter HI-crit mode
# All the possible combinations are tested (in Model 3 a single core entering
# HI-crit mode will interfere with all the others)
CORES_MODE_CHANGES = [
  ['c1', 'c2'],
  ['c1', 'c3'],
  ['c1', 'c4'],
  ['c2', 'c3'],
  ['c2', 'c4'],
  ['c2', 'c1'],
  ['c3', 'c1'],
  ['c3', 'c2'],
  ['c3', 'c4'],
  ['c4', 'c1'],
  ['c4', 'c2'],
  ['c4', 'c3']
]

# This is the configuration used to test the NO MIGRATION model
CORES_NO_MIGRATION = {
  'c1': {'tasks': [], 'considered': False, 'utilization': 0},
  'c2': {'tasks': [], 'considered': False, 'utilization': 0},
  'c3': {'tasks': [], 'considered': False, 'utilization': 0},
  'c4': {'tasks': [], 'considered': False, 'utilization': 0}
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
      ['c2', 'c3']
    ]
  },
  'c2': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c3', 'c4']
    ]
  },
  'c3': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c4', 'c1']
    ]
  },
  'c4': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c1', 'c2']
    ]
  }
}

# This is the configuration used to test MODEL 2
CORES_MODEL_2 = {
  'c1': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c2', 'c4'],
      ['c3', 'c4']
    ]
  },
  'c2': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c4', 'c3'],
      ['c1', 'c3']
    ]
  },
  'c3': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c1', 'c2'],
      ['c4', 'c2']
    ]
  },
  'c4': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c3', 'c1'],
      ['c2', 'c1']
    ]
  }
}

# This is the configuration used to test MODEL 3
CORES_MODEL_3 = {
  'c1': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c2', 'c3'],
      ['c2', 'c4'],
      ['c3', 'c2'],
      ['c3', 'c4'],
      ['c4', 'c2'],
      ['c4', 'c3']
    ]
  },
  'c2': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c3', 'c4'],
      ['c3', 'c1'],
      ['c1', 'c3'],
      ['c1', 'c4'],
      ['c4', 'c3'],
      ['c4', 'c1']
    ]
  },
  'c3': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c4', 'c1'],
      ['c4', 'c2'],
      ['c1', 'c2'],
      ['c1', 'c4'],
      ['c2', 'c1'],
      ['c2', 'c4']
    ]
  },
  'c4': {
    'tasks': [],
    'considered': False,
    'utilization': 0,
    'crit': False,
    'migration': [
      ['c1', 'c2'],
      ['c1', 'c3'],
      ['c2', 'c3'],
      ['c2', 'c1'],
      ['c3', 'c2'],
      ['c3', 'c1']
    ]
  }
}
