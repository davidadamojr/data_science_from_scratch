"""
Estimating the standard errors of our regression coefficients.
We repeatedly take a bootstrap_sample of our data and estimate beta based on 
that sample. If the coefficient corresponding to one of the independent variables 
does not vary much across samples, then we can be confident that our estimate is 
relatively tight.
"""

def estimate_sample_beta(sample):
    """ sample is a list of pairs (x_i, y_i) """
    x_sample, y_sample = zip(*sample)
    return estimate_beta(x_sample, y_sample)

random.seed(0) # so that you get the same results as me

bootstrap_betas = bootstrap_statistic(zip(x, daily_minutes_good),
                                      estimate_sample_beta,
                                      100)

# estimate the standard deviation of each coefficient
bootstrap_standard_errors = [standard_deviation([beta[i] for beta in bootstrap_betas]
                                                for i in range(4))]