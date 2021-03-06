"""
Run the nested cross-validation for the NMTF class, on the Sanger dataset.
"""

project_location = "/Users/thomasbrouwer/Documents/Projects/libraries/"
import sys
sys.path.append(project_location)

import numpy, itertools, random
from BNMTF.code.models.nmtf_np import NMTF
from BNMTF.code.cross_validation.nested_matrix_cross_validation import MatrixNestedCrossValidation
from BNMTF.experiments.experiments_gdsc.load_data import load_gdsc


# Settings
standardised = False
train_config = {
    'iterations' : 2000,
    'init_FG' : 'kmeans',
    'init_S' : 'exponential',
    'expo_prior' : 0.1
}
P = 5
no_folds = 10
output_file = "./results.txt"
files_nested_performances = ["./fold_%s.txt" % fold for fold in range(1,no_folds+1)]

# Construct the parameter search
parameter_search = [{'K':K,'L':L} for (K,L) in [(6,6), (8,8), (10,10)]]

# Load in the Sanger dataset
(_,X_min,M,_,_,_,_) = load_gdsc(standardised=standardised)

# Run the cross-validation framework
#random.seed(42)
#numpy.random.seed(9000)
nested_crossval = MatrixNestedCrossValidation(
    method=NMTF,
    X=X_min,
    M=M,
    K=no_folds,
    P=5,
    parameter_search=parameter_search,
    train_config=train_config,
    file_performance=output_file,
    files_nested_performances=files_nested_performances
)
nested_crossval.run()

"""
Average performances: {'R^2': 0.7948758708329315, 'MSE': 2.3988138408823394, 'Rp': 0.89178480273294591}. 
All performances: {'R^2': [0.7990403667846077, 0.7974592552426493, 0.7971559801700554, 0.7908843325029544, 0.7898394194643907], 'MSE': [2.3352752661466534, 2.3572503168518866, 2.4163844950465756, 2.4334280833191895, 2.4517310430473933], 'Rp': [0.89405814991652022, 0.89333868839901787, 0.89316370564203762, 0.88952291745977685, 0.88884055224737657]}. 

Average MSE: 2.3988 +- 0.0449
Averagr R^2: 0.795 +- 0.004
"""