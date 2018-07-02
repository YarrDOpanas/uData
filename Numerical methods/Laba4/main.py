import numpy as np
np.set_printoptions(precision=3)
try:
    A = np.loadtxt("matrix_exam_4.txt")
    b = np.loadtxt("vector_exam_4.txt")
except(Exception):
    print("Could not find file or invalid matrix")
    exit(-1)

print("Our matrix:\n", A)
print("Our vector:", b)
U, E, V = np.linalg.svd(A)
print("U:\n", U)
print("E:", E)
print("V:\n", V)
r = E[E > np.finfo(np.float32).eps].size
print("Rank of our matrix = " + str(r))
print("Condition number = " + str(E[E > np.finfo(np.float32).eps][0]/E[E > np.finfo(np.float32).eps][-1]))
if E.size == E[E > np.finfo(np.float32).eps].size:
    print("Our uniform system has no non zeros solutions")
else:
    print("Our uniform system has non zero solutions")
z = U.T @ b
print("z:", z)
if r == min(len(A), len(A[0])):
    y = z / E
    x = V.T @ y
    print("Our system is definite. X = ", x)
else:
    y = np.zeros(len(A[0]))
    y[:r] = z[:r] / E[E > np.finfo(np.float32).eps]
    x = x = V.T @ y
    if abs(z[r:-1]) < np.finfo(np.float32).eps:
        print("Our system is compatible.\n X = ",end = "")
        for i in range(r):
            print(round(y[i], 3), " * ",V.T[i],end = " + ")
        for i in range(r, len(A[0])):
            print('c'+str(i), " * ", V.T[i],end = " + ")
    else:
        print("Our system is not compatible. it's pseudo-resolves = ", x)
print("\nr = A*x - b=\n", A @ x - b)