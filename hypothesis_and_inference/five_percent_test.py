from probability_intervals import normal_upper_bound

hi = normal_upper_bound(0.95, mu_0, sigma_0)
# is 526 (< 531, since we need mroe probability in the upper tail)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)

power = 1 - type_2_probability   # 0.936