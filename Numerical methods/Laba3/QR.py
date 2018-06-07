import numpy as np
import math
import copy

def Hessenberg(B):
    '''Takes matrix as argument and returns matrix
    in the form of Hessenberg'''

    A = copy.deepcopy(B)
    b = np.sign(-A[1][0])*math.sqrt((A.T[0][1:] ** 2).sum())
    m = 1 / math.sqrt(2*b**2 - 2*A[1][0]*b)
    w = copy.copy(A.T[0])
    w[0] = 0
    w[1] = A[1][0] - b
    w *= m
    H = np.eye(A.__len__(), A.__len__()) - 2 * w.reshape(A.__len__(),1)*w
    A = H @ A @ H
    for i in range(1, A.__len__() - 1):
        b = np.sign(-A[i+ 1][i]) * math.sqrt((A.T[i][i+1:] ** 2).sum())
        m = 1/math.sqrt(2 * b**2 - 2 * A[i+1][i]*b)
        w = copy.copy(A.T[i])
        w[:i+1] = 0
        w[i + 1] = A[i+1][i] - b
        w *= m
        H = np.eye(A.__len__(), A.__len__()) - 2 * w.reshape(A.__len__(), 1) * w
        A = H @ A @ H
    return A