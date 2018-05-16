def print_matrix(A, text):
    '''As argument takes matrix and text you want to ouput
    with matrix'''

    print(text)
    for i in range(len(A)):
        for j in range(len(A[i])):
            print('{:>10}'.format(round(A[i][j], 7)), end = ' ')
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
        A = [[float(j) for j in input().split()] for i in range (n)]
    except(Exception):
        print('Invalid value')
        quit(1)
    return A

def input_matrix_from_file(filename):
    '''Inputing matrix from file. Takes filename as argument.
    Returns matrix or exception if can't'''

    data = []
    try:
        with open(filename) as f:
            for line in f:
                data.append([float(x) for x in line.split()])
    except Exception:
        print("Couldn't open file")
        quit(-1)
    return data