import numpy as np
import math
import copy

def Hessenberg(B):
    '''Takes matrix as argument and returns matrix
    in the form of Hessenberg'''

    A = copy.deepcopy(B)
    for i in range(0, A.__len__() - 2):
        if abs(np.sign(-A[i + 1, i])) > 10 ** (-8):
            b = np.sign(-A[i + 1, i]) * np.sqrt(np.power(A[i + 1:, i], 2).sum())
        else:
            b = np.sqrt(np.power(A[i + 1:, i], 2).sum())
        if abs(b) > 10 ** (-8):
            m = 1 / np.sqrt(2 * b ** 2 - 2 * A[i + 1, i] * b)
        else:
            m = 1
        w = copy.copy(A.T[i])
        w[:i+1] = 0
        w[i + 1] = A[i+1][i] - b
        w *= m
        H = np.eye(A.__len__(), A.__len__()) - 2 * w.reshape(A.__len__(), 1) * w
        A = H @ A @ H
    return A

def QR_iter(B):
   Q = np.eye(len(B))
   for l in range(len(B) - 1):
       if abs(B[l, l]) >= 10 ** (-8):
           t = B[l + 1, l] / B[l, l]
           c = 1 / np.sqrt(1 + t ** 2)
           s = t / np.sqrt(1 + t ** 2)
       else:
           c = 1
           s = 0
       T1 = np.eye(len(B))
       T1[l, l] = c
       T1[l + 1, l + 1] = c
       T1[l, l + 1] = s
       T1[l + 1, l] = -s
       B = np.dot(T1, B)
       Q = np.dot(Q, T1.T)
   A = np.dot(B, Q)
   return A


def QR(A):
   B = Hessenberg(A)
   print('Hessenberg: ')
   print(B)
   c = 0
   while np.abs(np.tril(B, -1).sum()) >= 10 ** (-4) and c < 10**3:
       B = QR_iter(B)
       c +=1
   return B

