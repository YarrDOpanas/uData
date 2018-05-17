import input_output as io
import math
import aditional_functions as af
import copy

def matrix_norm(A):
    '''Takes matrix as argument. Returns cubic norm of matrix.'''

    max = 0
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[0])):
            sum += abs(A[i][j])
        if sum > max:
            max = sum
    return max

def simple_iter_method(A, a):
    '''Takes SLAE via matrix and vector. Returns answer
    or False if can't'''

    B = []
    b = []
    for i in range(len(A)):
        B.append([ - A[i][j] / A[i][i] if i != j else 0 for j in range(len(A[0]))])
        b.append([a[i][0] / A[i][i]])
    q = matrix_norm(B)
    if q >= 1:
        print("Simple iteration method does not converge")
        quit(-1)
    e = 0.001
    k = round(math.log(e * (1 - q) / matrix_norm(b), q))
    print("Approximate number of steps = " + str(k))
    x = [[0] * 1 for i in range(len(A))]
    for i in range(k):
        y = copy.deepcopy(x)
        io.print_matrix(x, str(i) + " step: ")
        x = af.addition(af.multiplying(B, x), b)
        print("Epsilon = " + str(round(af.epsilon(x, y), 5)))
        print("--------------------")
    return x