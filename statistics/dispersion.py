import math
import sys
sys.path.insert(0, '../linear_algebra')

from central_tendencies import mean
from vector_operations import sum_of_squares

"""
Dispersion refers to measures of how spread out our data is
"""

def data_range(x):
    return max(x) - min(x)

# a more complex measure of dispersion is variance

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    """
    Variance has units that are the square of the original units. Since it can 
    be hard to make sense of such units, we often look instead at the standard 
    deviation.
    """
    return math.sqrt(variance(x))

def interquartile_range(x):
    """
    Both the range and standard deviation are greatly affected by outliers in data.
    A more robust alternative is the difference between the 75th percentile value 
    and the 25th percentile value - interquartile range
    """
    return quantile(x, 0.75) - quantile(x, 0.25)
    