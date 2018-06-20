import numpy as np
np.set_printoptions(precision=3)
try:
    A = np.loadtxt("matrix.txt")
    b1 = np.loadtxt("vector1.txt")
    b2 = np.loadtxt("vector2.txt")
except(Exception):
    print("Could not find file or invalid matrix")
    exit(-1)

print("Our matrix:\n", A)
print("Our vector1:", b1)
print("Our vector2:", b2)
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
z1 = U.T @ b1
print("z1:", z1)
z2 = U.T @ b2
print("z2:", z2)
print(len(A))
if r == min(len(A), len(A[0])):
    y = z1 / E
    x = V.T @ y
    print("Our system is compatible. X = ", x)
else:
    y = np.zeros(len(A[0]))
    y[:r] = z1[:r] / E[E > np.finfo(np.float32).eps]
    x = V.T @ y
    print("Our system is not compatible. it's pseudo-resolves = ", x)
