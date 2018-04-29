def print_matrix(A, text):
    '''As argument takes matrix and text you want to ouput
    with matrix'''

    print(text)
    for i in range(len(A)):
        for j in range(len(A[i])):
            print('{:>6}'.format(round(A[i][j], 3)), end = ' ')
        print()

def input_matrix():
    '''Input matix by lines. Every time input the whole line.
    Returns inputed matrix'''

    print("Input amount of lines: ")
    try:
        n = int(input())
    except(Exception):
        print('Invalid dimension')
        quit(1)
    if(n <= 0):
        print('Invalid dimension')
        quit(1)
    print('Input values: ')
    try:
        A = [[int(j) for j in input().split()] for i in range (n)]
    except(Exception):
        print('Invalid value')
        quit(1)
    return A

def changing_lines(A, B, i):
    '''Takes two matrix and index in witch A[i][i] == 0 as argument
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
    for j in range(len(A)):
        A_temp = A[index][j]
        A[index][j] = A[i][j]
        A[i][j] = A_temp
        A_temp = B[index][j]
        B[index][j] = B[i][j]
        B[i][j] = A_temp
    return A[i][i]

def Gauss(A, B):
    '''Takes two matrix as argument and transform them
    by Gauss method'''

    for i in range(len(A)):
        tmp = A[i][i]
        if tmp == 0:
            tmp = changing_lines(A, B, i)
        for k in range(len(A)):
            A[i][k] /= tmp
            B[i][k] /= tmp
        for k in range(len(A)):
            if k == i:
                continue
            a = A[k][i] / A[i][i]
            for j in range(len(A)):
                A[k][j] -= a * A[i][j]
                B[k][j] -= a * B[i][j]

def inversing(A):
    '''Takes matrix as argument and returns inversed one.
    Transforms source matrix into unit one'''

    for i in range(len(A)):
        if(len(A) != len(A[i])):
            print('Matrix should be square')
            quit(1)
    B = [[0]*len(A) for i in range(len(A))]
    for i in range(len(B)):
        B[i][i] = 1
    Gauss(A, B)
    return B

A = input_matrix()
print_matrix(A, "Matrix A:")
B = inversing(A)
print_matrix(B, "Matrix A^(-1): ")
print_matrix(A, "Matrix A after changes: ")