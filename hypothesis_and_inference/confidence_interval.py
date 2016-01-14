"""
We can estimate the probability of the unfair coin by looking at the 
average value of the Bernoulli variables corresponding to each flip - 1 if heads, 
0 if tails. If we observe 525 heads out of 1000 flips, then we estimate p equals 
0.525. How confident can we be about this estimate?
"""

from probability_intervals import normal_two_sided_bounds

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)  # 0.0158

normal_two_sided_bounds(0.95, mu, sigma) # [0.4940, 0.5560]

"""
Using the normal approximation, we conclude that we are "95% confident" that the 
above interval contains the true parameter p

We do not conclude that the coin is unfair because 0.5 falls within our confidence
interval.
"""

