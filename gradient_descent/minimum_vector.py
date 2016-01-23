import random
import sys

sys.path.insert(0, "../linear_algebra")
from vector_operations import distance

def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

# pick a random starting point
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)       # compute the gradient at v
    next_v = step(v, gradient, -0.01)           # take a negative gradient step
    if distance(next_v, v) < tolerance:         # stop if we're converging
        break
    v = next_v

print v