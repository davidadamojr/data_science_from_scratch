def p_value(beta_hat_j, sigma_hat_j):
    if beta_hat_j > 0:
        # if the coefficient is positive, we need to compute twice the 
        # probability of seeing an even *larger* value
        return 2 * (1 - normal_cdf(beta_hat_j / sigma_hat_j))
    else:
        # otherwise twice the probability of seeing a *smaller* value
        return 2 * normal_cdf(beta_hat_j / sigma_hat_j)
    
p_value(30.63, 1.174)       # ~0 (constant term)
p_value(0.972, 0.079)       # ~0 (num_friends)
p_value(-1.868, 0.131)      # ~0 (work hours)
p_value(0.911, 0.990)       # 0.36 (phd))