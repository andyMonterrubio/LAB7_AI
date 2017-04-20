#! /usr/bin/python
import random

'''
Algorithm
1)Initialize the weights and threshold to small random numbers.
2)Present a vector x to the neuron inputs and calculate the output.
3)Update the weights according to: formula
4)Repeat steps 2 and 3 until:
    -the iteration error is less than a user-specified error threshold or
    -a predetermined number of iterations have been completed.

'''


class Perceptron(object):
    def __init__(self):
        self.dimensionality = 0
        self.weights = []
        self.threshold = random.randrange(1, 10)


# returns 1 if perceptron is activated by inputs
def activation(perceptron, inputs):
    dot = 0
    for i in range(0, len(inputs)):
        dot += inputs[i] * perceptron.weights[i]
    if (dot > perceptron.threshold):
        return 1
    else:
        return 0


# updates perceptron's weights based on current error
# inputs must have the expected output on its last index
def update_weight(perceptron, inputs):
    desired_output = inputs[-1]
    actual_output = activation(perceptron, inputs[0:-1])
    error = desired_output - actual_output
    for i in range(0, len(perceptron.weights)):
        perceptron.weights[i] += error * inputs[i]
    return error


# read input file and run perceptron if possible
if __name__ == "__main__":
    perceptron = Perceptron()
    perceptron.dimensionality = int(input())

    # add random weights to perceptron
    for i in range(0, perceptron.dimensionality):
        perceptron.weights.append(random.randrange(-1, 2))

    training_size = int(input())
    test_size = int(input())

    training_set = []
    test_set = []

    # read training set
    for i in range(0, training_size):
        line = raw_input()

        training_set.append(line.split(','))
        training_set[i] = map(lambda x: float(x), training_set[i])

    # train perceptron until there's no error or 100 tries have passed
    iterations = 0
    while (iterations < 100):
        iterations += 1
        error = 0
        for i in range(0, training_size):
            error += pow(update_weight(perceptron, training_set[i]), 2)
        if (error == 0):
            break

    # read and run tests only if error is not too big
    if (error < 1):
        for i in range(0, test_size):
            line = raw_input()

            test_set.append(line.split(','))
            test_set[i] = map(lambda x: float(x), test_set[i])

            print activation(perceptron, test_set[i])
    else:
        print "no solution found"
