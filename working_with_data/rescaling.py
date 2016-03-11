"""
Sometimes units can affect the results of calculations.

When dimensions are not comparable with one another, we will sometimes rescale 
our data so that each dimension has mean 0 and standard deviation 1. This 
effectively gets rid of units, converting each dimension to "standard deviations 
from the mean"
"""

import sys
sys.path.insert(0, "../linear_algebra")
sys.path.insert(0, "../statistics")
from central_tendencies import mean
from dispersion import standard_deviation
from matrix_operations import get_column

def scale(data_matrix):
    # data matrix e.g. [[63,67,70], [160,170.2,177.8], [150,160,171]]
    
    """returns the means and standard deviations of each column"""
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j))
             for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j))
              for j in range(num_cols)]
    return means, stdevs

def rescale(data_matrix):
    """rescales the input data so that each column has mean 0 and standard 
    deviation 1, leaves alone columns with no deviation"""
    means, stdevs = scale(data_matrix)
    
    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j] / stdevs[j])
        else:
            return data_matrix[i][j]
    
    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)