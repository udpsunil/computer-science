# Simple neural network with multiple inputs
import vector_math

def w_sum(a, b):
    assert(len(a) == len(b))
    output = vector_math.vector_sum(vector_math.elementwise_multiplication(a,b))
    return output

# step 1: An empty network
weights = [0.1, 0.2, 0]

def neural_network(input, weights):
    prediction = w_sum(input, weights)
    return prediction

# step 2: inserting one input datapoint
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]
prediction = neural_network(input, weights)
print(prediction)

