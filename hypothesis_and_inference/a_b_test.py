from p_value import two_sided_p_value

"""
A/B test to choose which advertisement is more effective at getting clicks
"""

def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

"""
If "tastes great" gets 200 clicks out of 1000 views and "less bias" gets 180 
clicks out of 1000 views
"""
z = a_b_test_statistic(1000, 200, 1000, 180)   # -1.14

# the probability of seeing such a large difference if the means were actually
# equal
print two_sided_p_value(z)  # 0.254 - large enough to conclude there's a difference

# if "less bias" only got 150 clicks

z = a_b_test_statistic(1000, 200, 1000, 150) # -2.94
print two_sided_p_value(z)                   # 0.003 - probability you'd see such a large difference if the ads were equally effective'