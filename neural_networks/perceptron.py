"""
A perceptron approximates a single neuron with n binary inputs. It computes 
the weighted sum of its inputs and "fires" if that weighted sum is zero or 
greater.
"""

from linear_algebra.vector_operations import dot

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_output(weights, bias, x):
    """returns 1 if the perceptron 'fires', 0 if not"""
    calculation = dot(weights, x) + bias
    return step_function(calculation)