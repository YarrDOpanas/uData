import input_output as io
import copy
import aditional_functions as af

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