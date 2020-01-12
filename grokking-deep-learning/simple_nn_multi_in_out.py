# Predicting with multiple inputs and outputs

weights = [
 # toes, %win, fans
    [0.1, 0.1, -0.3],   # hurt?
    [0.1, 0.2, 0.0],    # win?
    [0.0, 1.3, 0.1]     # sad?
]

def w_sum(a, b):
    assert(len(a) == len(b))
    return sum([i*j for i,j in zip(a,b)])

def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    return [w_sum(vect, row) for row in matrix]

def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)

print(pred)
