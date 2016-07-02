import sys
sys.path.insert(0, '../gradient_descent')
from stochastic_gradient_descent import minimize_stochastic
import random

def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i, y_i, beta):
    """the gradient (with respect to beta) corresponding to the ith 
    squared error term"""
    return [-2 * x_ij * error(x_i, y_i, beta)
            for x_ij in x_i]

def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x]
    return minimize_stochastic(squared_error,
                               squared_error_gradient,
                               x, y,
                               beta_initial,
                               0.001)

random.seed(0)
x = [1,     # constant term 
     49,    # number of friends
     4,     # work hours per day
     0]     # does not have PhD
beta = estimate_beta(x, daily_minutes_good) # [30.63, 0.972, -1.868, 0.911]