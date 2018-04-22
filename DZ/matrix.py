#Multiplying matrix by the number

import random
print('Input the dimension of your matrix: ')
n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(round(random.random()*10))
print(a)
print('Input some number: ')
c = int(input())
for i in range(n):
    for j in range(n):
        a[i][j] *= c
print("New matrix: ", a)
