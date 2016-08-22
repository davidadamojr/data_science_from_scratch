import math
import sys
sys.path.insert(0, "../linear_algebra")

from vector_operations import dot

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, input_vector):
    """takes in a neural network (represented as a list of lists of weights)
    and returns the output from forward-propagating the input"""
    
    outputs = []
    
    # process one layer at a time
    for layer in neural_network:
        input_with_bias = input_vector + [1]        # add a bias input
        output = [neuron_output(neuron, input_with_bias)    # compute the output
                  for neuron in layer]
        outputs.append(output)                      # and remember it
        
        # then the input to the next layer is the output of this one
        input_vector = output
    
    return outputs