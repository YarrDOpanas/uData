import copy
import numpy as np

def Factorization(A):
    '''Takes as argument matrix, that should be factorized.
     Returns a tuple with two matrix, in witch A was factorised
     or False if it can't'''

    if len(A) != len(A[0]):
        return (False, False)
    U = copy.deepcopy(A)
    L = [[0] * len(U[0]) for i in range(len(U))]
    for i in range(len(U)):
        if abs(U[i][i]) < np.finfo(np.float32).eps:
            return (False, False)
        L[i][i] = 1
        for k in range(i + 1, len(U)):
            L[k][i] = U[k][i] / U[i][i]
            for j in range(i, len(U[0])):
                U[k][j] -= L[k][i] * U[i][j]
    return (L, U)

def Inversed_matrix(L, U):
    '''Takes L and U as argument and returns inversed matrix'''

    A = [[0]* len(U) for  i in range (len(U))]
    for k in range(len(U)):
        e = [1 if j == k else 0 for j in range(len(U))]
        y = []
        y.append([])
        y[0].append(e[0])
        for i in range(1, len(U)):
            sum = 0
            for j in range(i):
                sum += L[i][j] * y[j][0]
            y.append([])
            y[i].append(e[i] - sum)
        e[-1] = y[-1][0] / U[-1][-1]
        for i in range(len(U) - 2, -1, -1):
            sum = 0
            for j in range(i + 1, len(U)):
                sum += e[j] * U[i][j]
            e[i] = 1 / U[i][i] * (y[i][0] - sum)
        for i in range(len(U)):
            A[i][k] = e[i]
    return A

def matrix_norm(A):
    '''Takes matrix as argument and returns it's
    octahedral norm.'''

    max = 0
    for j in range(len(A[0])):
        sum = 0
        for i in range(len(A)):
            sum += abs(A[i][j])
        if sum > max:
            max = sum
    return max

def solution(L, U, b):
    '''Takes as argument A matrix via LU-factorization
    and column of free numbers. Returns matrix of answers'''

    y = []
    y.append([])
    y[0].append(b[0][0])
    for i in range(1, len(U)):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j][0]
        y.append([])
        y[i].append(b[i][0] - sum)
    x = [[0] * 1 for i in range(len(U))]
    x[-1][0] = y[-1][0] / U[-1][-1]
    for i in range(len(U) - 2, -1, -1):
        sum = 0
        for j in range(i + 1, len(U)):
            sum += x[j][0] * U[i][j]
        x[i][0] = 1 / U[i][i] * (y[i][0] - sum)
    return x