from probability_intervals import normal_probability_above
from probability_intervals import normal_probability_below

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)
    
# two sided p-value for 530 heads in 1000 trials of coin flip
print two_sided_p_value(529.5, 50, 15.8)