import math

def uniform_pdf(x):
    "Uniform probability density function for continuous distribution"""
    
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    "returns the probability that a uniform random variable is <=x"
    if x < 0: return 0      # uniform random is never less than 0
    elif x < 1: return x    # e.g. P(X <= 0.4) = 0.4)
    else: return 1          # uniform random is always less than 1
    
def normal_pdf(x, mu=0, sigma=1):
    """
    Classic bell curve-shaped distribution.
    The mean (mu) indicates where the bell is centered.
    The standard deviation (sigma) shows how wide the bell is.
    """
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """
    Sometimes we'll need to invert normal_cdf to find the value corresponding 
    to a specified probability. 
    
    Find approximate inverse using binary search
    """
    
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z, low_p = -10.0, 0             # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1                # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2      # consider the midpoint
        mid_p = normal_cdf(mid_z)       # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
        
    return mid_z