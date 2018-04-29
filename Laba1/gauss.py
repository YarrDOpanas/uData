import copy
import input_output as io
def Gauss(A, a):
    B = copy.deepcopy(A)
    b = copy.deepcopy(a)
    for i in range(len(B) - 1):
        for k in range(i + 1, len(B)):
            temp = B[k][i] / B[i][i]
            b[k] -= temp * b[i]
            for j in range(i, len(B)):
                B[k][j] -= temp * B[i][j]
    x = [0] * len(b)
    x[-1] = b[-1] / B[-1][-1]
    for i in range(len(B) - 2, -1, -1):
        sum = 0
        for j in range(i + 1, len(B)):
            sum += B[i][j] * x[j]
        x[i] = 1 / B[i][i] * (b[i] - sum)
    io.print_matrix(B, "koko")