import copy
def input_matrix(n, m):
    A = []
    for i in range(n):
        A.append([])
        for j in range(m):
            A[i].append(float(input()))
    return A

def multiplying(A, B):
    #C = copy.deepcopy(A)
    if len(A[0]) != len(B):
        print('Wrong dimension')
        quit(228)
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append([])
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k] * B[k][j]
            C[i][j] = sum
    return C

def E_matrix(n, m):
    E = []
    for i in range(n):
        E.append([])
        for j in range(m):
            E[i].append(0)
        E[i][i] = 1
    return E

n = int(input())
m = int(input())
print(E_matrix(n, m))

A = input_matrix(2, 3)
# B = input_matrix(3, 1)
# C = multiplying(A, B)
# print(A)
# print(B)
# print(C)
B = copy.deepcopy(A)
print(B)




