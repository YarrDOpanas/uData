import numpy as np
import copy
import math

def Jacobi(B):
    '''Takes symmetric matrix as argument. Returns
    matrix of eigenvalues and diagonal matrix of eigenvectors.'''

    if(not np.allclose(B, B.T)):
        raise Exception("Matirx is assymetric")
    A = copy.deepcopy(B)
    a_max = np.amax(np.absolute(np.triu(A, 1)))         # Достает максимальный по модулю елемент из
                                                        # верхней треугольной матрицы
    X = np.eye(A.__len__(), A.__len__())
    k = 1
    print("Jacobi:\n")
    while a_max > np.finfo(float).eps:
        i = np.where(np.absolute(A) == np.amax(np.absolute(np.triu(A, 1))))[0][0]   #Узнаем индексы
        j = np.where(np.absolute(A) == np.amax(np.absolute(np.triu(A, 1))))[1][0]   #максимального елемента
        fi = math.atan(2 * A[i][j]/(A[i][i] - A[j][j])) / 2
        H = np.eye(A.__len__(), A.__len__())
        H[i][i] = H[j][j] = math.cos(fi)
        H[i][j] = -math.sin(fi)
        H[j][i] = math.sin(fi)
        A = H.T @ A @ H
        X = X @ H
        print(str(k) + " iteration -------------")
        print("A_max_element = " + str(round(a_max, 6)))
        print("Trace of a matrix = " + str(round(np.diag(A).sum(), 3)))
        print("Euclidean norm = " + str(round(np.linalg.norm(A), 3)))
        a_max = np.amax(np.absolute(np.triu(A, 1)))
        k += 1
    return A, X