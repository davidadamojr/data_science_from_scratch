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