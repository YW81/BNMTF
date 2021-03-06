"""
Run the cross validation with line search for model selection using VB-NMF on
the CCLE EC50 dataset.
"""

project_location = "/Users/thomasbrouwer/Documents/Projects/libraries/"
import sys
sys.path.append(project_location)

import numpy, random
from BNMTF.code.models.bnmf_vb_optimised import bnmf_vb_optimised
from BNMTF.code.cross_validation.line_search_cross_validation import LineSearchCrossValidation
from BNMTF.experiments.experiments_ccle.load_data import load_ccle


# Settings
standardised = False
iterations = 1000
init_UV = 'random'

K_range = [1,2,3]
no_folds = 10
restarts = 1

quality_metric = 'AIC'
output_file = "./results.txt"

alpha, beta = 1., 1.
lambdaU = 1./10.
lambdaV = 1./10.
priors = { 'alpha':alpha, 'beta':beta, 'lambdaU':lambdaU, 'lambdaV':lambdaV }

# Load in the CCLE EC50 dataset
R,M = load_ccle(ic50=False)

# Run the cross-validation framework
#random.seed(42)
#numpy.random.seed(9000)
nested_crossval = LineSearchCrossValidation(
    classifier=bnmf_vb_optimised,
    R=R,
    M=M,
    values_K=K_range,
    folds=no_folds,
    priors=priors,
    init_UV=init_UV,
    iterations=iterations,
    restarts=restarts,
    quality_metric=quality_metric,
    file_performance=output_file
)
nested_crossval.run()
