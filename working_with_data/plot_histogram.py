from buckets import *
import random
import sys
sys.path.insert(0, '../probability')

from distributions import inverse_normal_cdf

"""
Knowing the max, min, mean and standard deviation is often not enough to show 
distinct characteristics of data.

These two sets of data have means close to 0 and standard deviations close to 
58. However, they have very different distributions
"""

random.seed(0)

# uniform between -100 and 100
uniform = [200 * random.random() - 100 for _ in range(1000)]

# normal distribution with mean 0, standard deviation 57
normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]

plot_histogram(uniform, 10, "Uniform Histogram")
plot_histogram(normal, 10, "Normal histogram")