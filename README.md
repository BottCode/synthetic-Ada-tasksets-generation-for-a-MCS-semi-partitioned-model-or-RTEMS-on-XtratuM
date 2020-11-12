This script attempts to reproduce the results described in the 2019 paper by H. Xu and A. Burns titled ["A semi-partitioned model for mixed criticality systems"](https://www.sciencedirect.com/science/article/pii/S0164121219300020).

## Requirements
The script runs on [python3](https://www.python.org/download/releases/3.0/) and needs the following additional packages:
* [numpy](https://numpy.org/) -> `pip3 install numpy`
* [matplotlib](https://matplotlib.org/) -> `pip3 install matplotlib`
* [progress](https://pypi.org/project/progress/) -> `pip3 install progress`
* [joblib](https://joblib.readthedocs.io/en/latest/index.html) -> `pip3 install joblib`

## Usage
To launch the script with the default configuration (in optimized version):
```bash
$ cd path/to/script/directory
$ python3 -O ./run.py
```

To launch the script with the assertion checks:
```bash
$ cd path/to/script/directory
$ python3 ./run.py
```

The script will run the four tests described in the paper and produce as results four charts which will be saved at a configurable path (cfr. [Configuration](#configuration)).

## Unit tests
To run the unit tests for the RTA algorithms:
```bash
$ cd path/to/script/directory
$ python3 ./test.py
```

## Configuration
The file `config.py` defines some options for the script:
* `PARALLEL_JOBS` defines the number of parallel tests to be run (defaults to the number of CPUs)
* `VESTAL_CLASSIC`, `VESTAL_WITH_MONITOR`, `ALWAYS_HI_CRIT` defines which version of Vestal's algorithm should be used for the non migrating tests
* `CHECK_NO_MIGRATION`, `CHECK_MODEL_1`, etc. defines which models to test
* `RUN_FIRST_TEST`, `RUN_SECOND_TEST`, etc. defines which tests to run
* `FIRST_FIT_BP`, `WORST_FIT_BP` defines which bin-packing algorithm to use
* `RESULTS_DIR` defines where to save the results
* `CORES_MODE_CHANGES` holds the possible sequences of core mode change
* `CORES_NO_MIGRATION`, `CORES_MODEL_1`, etc. defines the configurations used to test the different models

## Additions by [Mattia Bottaro](https://github.com/BottCode)

For my master's degree project in CS, I have to compare an implementation, made by myself, of the ["Semi-partitioned model for *dual-core* mixed criticality system"](https://dl.acm.org/doi/10.1145/2834848.2834865) and [XtratuM](https://fentiss.com/products/hypervisor), which is a TSP. [Gabriele Pozzan](https://github.com/cornacchia)'s work, which concerns experiments on Semi-partitioned model [quad-core version](https://www.sciencedirect.com/science/article/abs/pii/S0164121219300020), is also partly useful to me, especially the parts of tasket generation, priority assignement and some RTAs. So I am adapting his work according to my needs. You can find my additions on `$ROOT/dual-core-version/`