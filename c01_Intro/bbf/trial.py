import os
import sys

import nni

# For NNI use relative import for user-defined modules
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../..'
sys.path.append(SCRIPT_DIR)
from black_box_function import black_box_function

if __name__ == '__main__':
    # parameter from the search space selected by tuner
    p = nni.get_next_parameter()
    x = p['x']
    y = p['y']
    z = p['z']
    r = black_box_function(x, y, z)
    # returning result to NNI
    nni.report_final_result(r)
