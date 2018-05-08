import copy

def Factorization(A):
    '''Takes as argument matrix, that should be factorized.
     Returns a tuple with two matrix, in witch A was factorised
     or False if it can't'''

    if len(A) != len(A[0]):
        return (False, False)
    U = copy.deepcopy(A)
    L = [[0] * len(U[0]) for i in range(len(U))]
    for i in range(len(U)):
        if U[i][i] == 0:
            return (False, False)
        L[i][i] = 1
        for k in range(i + 1, len(U)):
            L[k][i] = U[k][i] / U[i][i]
            for j in range(i, len(U[0])):
                U[k][j] -= L[k][i] * U[i][j]
    return L, U

def Inversed_matrix(L, U):
    '''Takes L and U as argument and returns inversed matrix'''

    E = [[0]*len(U[0]) for i in range(len(U))]
    for i in range(len(U)):
        E[i][i] = 1
    Y = []
    for k in range(len(U)):
        Y.append([])
        Y[k].append(E[k][0])
        for i in range(1, len(L)):
            sum = 0
            for j in range(i):
                sum += L[i][j] * Y[k][j]
            Y[k].append(E[k][i] - sum)
    #to be continued...
