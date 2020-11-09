""" Generation of example data

"""

import random

import pandas as pd


# Settings #
############

n_samples = 100
x_values = list(range(n_samples))


# Random Data Generation #
##########################

# fix random number generation
random.seed(42)

# b + m * x + e: gauss rising
sample_a = [0 + 1 * xx + random.gauss(0, 3) for xx in x_values]

# b + x * m + e: gauss falling slightly
sample_b = [50 - 0.1 * xx + random.gauss(0, 9) for xx in x_values]

# b + x * m + e: uniform constant
sample_c = [80 - 0 * xx + random.uniform(-3, 3) for xx in x_values]

# combine to frame
sample_frame = pd.DataFrame({'x': x_values, 'a': sample_a, 'b': sample_b, 'c': sample_c})
