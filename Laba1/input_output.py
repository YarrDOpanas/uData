def print_matrix(A, text):
    '''As argument takes matrix and text you want to ouput
    with matrix'''

    print(text)
    for i in range(len(A)):
        for j in range(len(A[i])):
            print('{:>6}'.format(round(A[i][j], 3)), end = ' ')
        print()

def Input_matrix_from_keyboard():
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

#def input_matrix_from_file(filename):