def elementwise_multiplication(vec_a, vec_b):
    return [i*j for i, j in zip(vec_a, vec_b)]

def elementwise_addition(vec_a, vec_b):
    return [i+j for i, j in zip(vec_a, vec_b)]

def vector_sum(vec_a):
    return sum(vec_a)

def vector_average(vec_a):
    return sum(vec_a) / len(vec_a)


if __name__ == "__main__":
    vec_a = [1, 2, 3]
    vec_b = [3, 2, 1]
    print(elementwise_multiplication(vec_a, vec_b))
    print(elementwise_addition(vec_a, vec_b))
    print(vector_sum(vec_a))
    print(vector_average(vec_a))
    