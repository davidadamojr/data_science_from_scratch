from feed_forward import feed_forward

xor_network = [# hidden layer
               [[20, 20, -30],          # 'and' neuron
                [20, 20, -10]],         # 'or' neuron
               # output layer
               [[-60, 60, -30]]]        # '2nd input but not 1st input' neuron

for x in [0, 1]:
    for y in [0, 1]:
        # feed_forward produces the output of every neuron
        # feed_forward[-1] is the outputs of the output-layer neurons
        print x, y, feed_forward(xor_network, [x, y])[-1]
        