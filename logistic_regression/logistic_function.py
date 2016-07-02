import math

def logistic(x):
    return 1.0 / (1 + math.exp(-x))

def logistic_prim(x):
    return logistic(x) * (1 - logistic(x))