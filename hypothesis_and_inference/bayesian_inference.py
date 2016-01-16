"""
An alternative approach to inference involves treating the unknown parameters 
themselves as random variables. We start with a prior distribution for the 
parameters and then use the observed data and Bayes's theorem to get an updated 
posterior distribution for the parameters.

When the unknown parameter is a probabilty, we often use a prior from the beta 
distribution, which puts all its probability between 0 and 1
"""

def B(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:              # no weight outside of [0, 1]
        return 0
    
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)