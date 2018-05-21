import input_output as io
import copy
import aditional_functions as af
def coefficient(B):
    '''Takes matrix as argument ab returns
    coefficient for epsilon'''

    max = 0
    for i in range(len(B)):
        sum1 = 0
        sum2 = 0
        for j in range(len(B[0])):
            if j == i:
                sum2 = sum1
            sum1 += abs(B[i][j])
        q = sum1 / (1 - sum2)
        if q > max:
            max = q
    return (1 - max) / max

def zaidel(A, a):
    '''Takes as argument SLAE as matrix and vector. Returns
    answer via zaidel method or false if can't'''

    B = []
    b = []
    for i in range(len(A)):
        B.append([ - A[i][j] / A[i][i] if i != j else 0 for j in range(len(A[0]))])
        b.append([a[i][0] / A[i][i]])
    e = 0.001
    x = [[0]* 1 for i in range(len(A))]
    eps = 1
    step = 0
    #q = coefficient(B)
    while eps > e:
        step += 1
        y = copy.deepcopy(x)
        for i in range(len(A)):
            sum = 0
            for j in range(len(A[0])):
                sum += B[i][j] * x[j][0]
            x[i][0] = sum + b[i][0]
        eps = af.epsilon(x, y)
        io.print_matrix(x, str(step) + " step: ")
        print("Epsilon = " + str(round(eps, 5)))
        print("--------------------")
    return x