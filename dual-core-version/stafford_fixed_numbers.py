import numpy as np
import random
import math
import sys
import oct2py

def StaffordRandFixedSum (n, m, s, a, b):
    oc = oct2py.Oct2Py()
    utils = []

    for v in oc.stafford(n, m, s, a, b):
        utils.append (v[0])

    return utils