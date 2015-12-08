from __future__ import division
import sys
sys.path.insert(0, '../linear_algebra')

from vector_operations import dot
from dispersion import de_mean
from dispersion import standard_deviation 

def covariance(x, y):
    """
    Whereas variance measures how a single variable deviates from its mean, 
    covariance measures how two variables vary in tandem from their means.
    
    A "large" positive covariance means that x tends to be large when  y is large 
    and small when y is small. A "large" negative covariance means the opposite - 
    that x tends to be small when y is large and vice versa. A covariance close to 
    zero means no such relationship exists.
    """
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    """
    Covariance values are sometimes difficult to interprete. For this reason, 
    correlation is a more common measure.
    
    Correlation is always unitless and always lies between -1 (perfect anti-correlation) 
    and 1 (perfect correlation). Correlation is sensitive to outliers.
    """
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero