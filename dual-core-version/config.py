import multiprocessing

# Set number of parallel jobs
# Watchout: in dual-core version PARALLEL_JOBS must set to 1.
PARALLEL_JOBS = 1 # multiprocessing.cpu_count()

# Enable/disable models to check
CHECK_NO_MIGRATION = False
CHECK_SEMI_1_BF    = False
CHECK_SEMI_1_FF    = False
CHECK_SEMI_2_FF    = False
CHECK_SEMI_2_BF    = False

CHECK_SEMI_1_WF    = False
CHECK_SEMI_2_WF    = False

# https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/13
CHECK_HIERARCHICAL_SCHEDULING_OFFSET_BASED_MAST = True

NUMBER_OF_APPROACHES = 7

# Enable/disable tests to run
RUN_FIRST_TEST = True
RUN_SECOND_TEST = False
RUN_THIRD_TEST = False
RUN_FOURTH_TEST = False

# Select bin-packing algorithm to use
FIRST_FIT_BP = False
BEST_FIT_BP  = False 
WORST_FIT_BP = True

# Select version of Vestal's algorithm to use
VESTAL_CLASSIC = False
VESTAL_WITH_MONITOR = False
# Always consider HI-crit interference from HI-crit tasks
# Only ALWAYS_HI_CRIT is refined with RTE overhead in its RTA
# see <https://gitlab.com/thesisBottaroMattia/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/-/issues/1>
ALWAYS_HI_CRIT = True

PLATFORM = "RTE-SPM-Zynq7000"

# Number of tests to run for each Utilization step
NUMBER_OF_TESTS = 1

# Results will be saved in RESULTS_DIR
RESULTS_DIR = './results_dualcore_2/'

UTIL_STEP = 0.012
UTIL_LOWER_BOUND = 1.6
UTIL_HIGHER_BOUND = 2.2

CRITICALITY_STEP = 0.25
CRITICALITY_LOWER_BOUND = 1.5
CRITICALITY_HIGHER_BOUND = 4

PROPORTION_STEP = 0.1
PROPORTION_LOWER_BOUND = 0.1
PROPORTION_HIGHER_BOUND = 0.9

TASKSETS_SIZE = [21, 22, 23, 24]

TASK_MIN_REAL_UTILIZATION = 0.30
TASK_MAX_REAL_UTILIZATION = 0.90

STEPS = 0

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
slices_duration = {
  'c1': {'LOW': 0, 'HIGH': 0}, # milliseconds
  'c2': {'LOW': 0, 'HIGH': 0}
}

XML_Files = {
  1: {
    'nomigration': './XML_tasksets/experiment_1/nomigration.xml',
    'semi1FF': './XML_tasksets/experiment_1/semi1-FF.xml',
    'semi1BF': './XML_tasksets/experiment_1/semi1-BF.xml',
    'semi1WF': './XML_tasksets/experiment_1/semi1-WF.xml',
    'semi2FF': './XML_tasksets/experiment_1/semi2-FF.xml',
    'semi2BF': './XML_tasksets/experiment_1/semi2-BF.xml',
    'semi2WF': './XML_tasksets/experiment_1/semi2-WF.xml'
  },

  2: {
    'nomigration': './XML_tasksets/experiment_2/nomigration.xml',
    'semi1FF': './XML_tasksets/experiment_2/semi1-FF.xml',
    'semi1BF': './XML_tasksets/experiment_2/semi1-BF.xml',
    'semi1WF': './XML_tasksets/experiment_2/semi1-WF.xml',
    'semi2FF': './XML_tasksets/experiment_2/semi2-FF.xml',
    'semi2BF': './XML_tasksets/experiment_2/semi2-BF.xml',
    'semi2WF': './XML_tasksets/experiment_2/semi2-WF.xml'
  },
  
  3: {
    'nomigration': './XML_tasksets/experiment_3/nomigration.xml',
    'semi1FF': './XML_tasksets/experiment_3/semi1-FF.xml',
    'semi1BF': './XML_tasksets/experiment_3/semi1-BF.xml',
    'semi1WF': './XML_tasksets/experiment_3/semi1-WF.xml',
    'semi2FF': './XML_tasksets/experiment_3/semi2-FF.xml',
    'semi2BF': './XML_tasksets/experiment_3/semi2-BF.xml',
    'semi2WF': './XML_tasksets/experiment_3/semi2-WF.xml'
  },

  4: {
    'nomigration': './XML_tasksets/experiment_4/nomigration.xml',
    'semi1FF': './XML_tasksets/experiment_4/semi1-FF.xml',
    'semi1BF': './XML_tasksets/experiment_4/semi1-BF.xml',
    'semi1WF': './XML_tasksets/experiment_4/semi1-WF.xml',
    'semi2FF': './XML_tasksets/experiment_4/semi2-FF.xml',
    'semi2BF': './XML_tasksets/experiment_4/semi2-BF.xml',
    'semi2WF': './XML_tasksets/experiment_4/semi2-WF.xml'
  },
}

Ada_Paths = {
  1: {
    'nomigration': './Ada_tasksets/experiment_1/nomigration/',
    'semi1FF': './Ada_tasksets/experiment_1/semi1-FF/',
    'semi1BF': './Ada_tasksets/experiment_1/semi1-BF/',
    'semi1WF': './Ada_tasksets/experiment_1/semi1-WF/',
    'semi2FF': './Ada_tasksets/experiment_1/semi2-FF/',
    'semi2BF': './Ada_tasksets/experiment_1/semi2-BF/',
    'semi2WF': './Ada_tasksets/experiment_1/semi2-WF/'
  },

  2: {
    'nomigration': './Ada_tasksets/experiment_2/nomigration/',
    'semi1FF': './Ada_tasksets/experiment_2/semi1-FF/',
    'semi1BF': './Ada_tasksets/experiment_2/semi1-BF/',
    'semi1WF': './Ada_tasksets/experiment_2/semi1-WF/',
    'semi2FF': './Ada_tasksets/experiment_2/semi2-FF/',
    'semi2BF': './Ada_tasksets/experiment_2/semi2-BF/',
    'semi2WF': './Ada_tasksets/experiment_2/semi2-WF/'
  },
  
  3: {
    'nomigration': './Ada_tasksets/experiment_3/nomigration/',
    'semi1FF': './Ada_tasksets/experiment_3/semi1-FF/',
    'semi1BF': './Ada_tasksets/experiment_3/semi1-BF/',
    'semi1WF': './Ada_tasksets/experiment_3/semi1-WF/',
    'semi2FF': './Ada_tasksets/experiment_3/semi2-FF/',
    'semi2BF': './Ada_tasksets/experiment_3/semi2-BF/',
    'semi2WF': './Ada_tasksets/experiment_3/semi2-WF/'
  },

  4: {
    'nomigration': './Ada_tasksets/experiment_4/nomigration/',
    'semi1FF': './Ada_tasksets/experiment_4/semi1-FF/',
    'semi1BF': './Ada_tasksets/experiment_4/semi1-BF/',
    'semi1WF': './Ada_tasksets/experiment_4/semi1-WF/',
    'semi2FF': './Ada_tasksets/experiment_4/semi2-FF/',
    'semi2BF': './Ada_tasksets/experiment_4/semi2-BF/',
    'semi2WF': './Ada_tasksets/experiment_4/semi2-WF/'
  },
}

Ada_No_Mig_Paths = {
  1: {
    'nomigration': './Ada_tasksets_no_mig/experiment_1/nomigration/',
    'semi1FF': './Ada_tasksets_no_mig/experiment_1/semi1-FF/',
    'semi1BF': './Ada_tasksets_no_mig/experiment_1/semi1-BF/',
    'semi1WF': './Ada_tasksets_no_mig/experiment_1/semi1-WF/',
    'semi2FF': './Ada_tasksets_no_mig/experiment_1/semi2-FF/',
    'semi2BF': './Ada_tasksets_no_mig/experiment_1/semi2-BF/',
    'semi2WF': './Ada_tasksets_no_mig/experiment_1/semi2-WF/'
  },

  2: {
    'nomigration': './Ada_tasksets_no_mig/experiment_2/nomigration/',
    'semi1FF': './Ada_tasksets_no_mig/experiment_2/semi1-FF/',
    'semi1BF': './Ada_tasksets_no_mig/experiment_2/semi1-BF/',
    'semi1WF': './Ada_tasksets_no_mig/experiment_2/semi1-WF/',
    'semi2FF': './Ada_tasksets_no_mig/experiment_2/semi2-FF/',
    'semi2BF': './Ada_tasksets_no_mig/experiment_2/semi2-BF/',
    'semi2WF': './Ada_tasksets_no_mig/experiment_2/semi2-WF/'
  },
  
  3: {
    'nomigration': './Ada_tasksets_no_mig/experiment_3/nomigration/',
    'semi1FF': './Ada_tasksets_no_mig/experiment_3/semi1-FF/',
    'semi1BF': './Ada_tasksets_no_mig/experiment_3/semi1-BF/',
    'semi1WF': './Ada_tasksets_no_mig/experiment_3/semi1-WF/',
    'semi2FF': './Ada_tasksets_no_mig/experiment_3/semi2-FF/',
    'semi2BF': './Ada_tasksets_no_mig/experiment_3/semi2-BF/',
    'semi2WF': './Ada_tasksets_no_mig/experiment_3/semi2-WF/'
  },

  4: {
    'nomigration': './Ada_tasksets_no_mig/experiment_4/nomigration/',
    'semi1FF': './Ada_tasksets_no_mig/experiment_4/semi1-FF/',
    'semi1BF': './Ada_tasksets_no_mig/experiment_4/semi1-BF/',
    'semi1WF': './Ada_tasksets_no_mig/experiment_4/semi1-WF/',
    'semi2FF': './Ada_tasksets_no_mig/experiment_4/semi2-FF/',
    'semi2BF': './Ada_tasksets_no_mig/experiment_4/semi2-BF/',
    'semi2WF': './Ada_tasksets_no_mig/experiment_4/semi2-WF/'
  },
}

MAST_analysis_path = {
  1: './mast_analysis/experiment_1/',

  2: './mast_analysis/experiment_2/',
  
  3: './mast_analysis/experiment_3/',

  4: './mast_analysis/experiment_4/'
}

Ada_RTEMS_XM_Paths = {
  1: {
    'nomigration': '../../TSP/Ada_tasksets/experiment_1/nomigration/'
  },

  2: {
    'nomigration': '../../TSP/Ada_tasksets/experiment_2/nomigration/'
  },
  
  3: {
    'nomigration': '../../TSP/Ada_tasksets/experiment_3/nomigration/'
  },

  4: {
    'nomigration': '../../TSP/Ada_tasksets/experiment_4/nomigration/'
  },
}

Ada_RTEMS_Common_Folder = '../../TSP/Ada_tasksets/common/'

EXPERIMENTS_REPETITIONS = 10

GLOBAL_TASKSET_ID = 0

RUNTIME_DIR = ''

RUNTIME_NO_MIG_DIR = ''

# TSP schemes are described in section 2.2.3 of this document:
# https://gitlab.com/thesisBottaroMattia/mcs-vs-tsp-a-comparison/-/issues/8
# Supported schemes:
#   - 1 -> 1 core, 1 partition
#   - 2 -> a partition for each criticality level
TSP_SCHEMA = 2
TSP_PLATFORM = "XtratuM"
# integer, milliseconds
TEMPORAL_SLICE_SIZE = 5
