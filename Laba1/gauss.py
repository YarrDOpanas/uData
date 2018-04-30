import copy
import input_output as io

def changing_lines(A, b, i):
    '''Takes matrix, vector and index in witch A[i][i] == 0 as argument
    and findes line with the highest value. Returns it.
    Terminates program if it is 0.'''

    max = 0
    index = i
    for m in range(i + 1, len(A)):
        if A[m][i] > max:
            max = A[m][i]
            index = m
    if max == 0:
        print("This matrix is degenerate, it hasn't inversed one")
        quit(1)
    temp = b[index]
    b[index] = b[i]
    b[i] = temp
    for j in range(len(A)):
        temp = A[index][j]
        A[index][j] = A[i][j]
        A[i][j] = temp
    return index

def Gauss(A, a):
    B = copy.deepcopy(A)
    b = copy.deepcopy(a)
    for i in range(len(B) - 1):
        if B[i][i] == 0:
            index  = changing_lines(B, b, i)
        for k in range(i + 1, len(B)):
            temp = B[k][i] / B[i][i]
            b[k] -= temp * b[i]
            for j in range(i, len(B)):
                B[k][j] -= temp * B[i][j]
    if B[-1][-1] == 0:
        print("This matrix is degenerate, it hasn't inversed one")
        quit(len(B))
    x = [0] * len(b)
    x[-1] = b[-1] / B[-1][-1]
    for i in range(len(B) - 2, -1, -1):
        sum = 0
        for j in range(i + 1, len(B)):
            sum += B[i][j] * x[j]
        x[i] = 1 / B[i][i] * (b[i] - sum)
    io.print_matrix(B, "check: ")
    io.print_vector(b, "b: ")
    return x