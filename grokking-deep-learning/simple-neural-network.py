# Simple neural network 

# step 1: An empty network
weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction

# step 2: inserting one input datapoint
number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]
prediction = neural_network(input, weight)
print(prediction)
