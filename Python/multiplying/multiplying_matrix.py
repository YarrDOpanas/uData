#Multiplying matrix

import random

def input_matrix():
    print("Input the dimension:\nN: ")
    size1 = int(input())
    print("M: ")
    size2 = int(input())
    A = []
    for i in range(size1):
        A.append([])
        for j in range(size2):
            A[i].append(round(random.random()*10))
    print("Your matrix: ", A)
    return A
A = input_matrix()
B = input_matrix()
def multiplying(A, B):
    if(len(A[0]) != len(B)):
        return False
    tmp = []
    for i in range(len(A)):
        tmp.append([])
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum = sum + A[i][k] * B[k][j]
            tmp[i].append(sum)
    return tmp
C = multiplying(A, B)
print(C) if C else print("Wrong dimension, can't be multiplied")