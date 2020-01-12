# Making single prediction with multiple outputs

weights = [0.3, 0.2, 0.9]

def ele_mul(number, vector):
    return [number*i for i in vector]
    

def neural_network(input, weights):
    pred = ele_mul(input, weights)
    return pred

wlrec = [0.65, 0.8, 0.8, 0.9]
input = wlrec[0]
pred = neural_network(input, weights)
print(pred)
