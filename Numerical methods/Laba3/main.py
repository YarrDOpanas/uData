import numpy as np
import Jacobi
import  math
np.set_printoptions(precision=3)

try:
    A = np.loadtxt("matrix.txt")
except(Exception):
    print("Could not find file or invalid matrix")
    exit(-1)
print("Our matrix:")
print(A)
try:
    L, X = Jacobi.Jacobi(A)
except Exception as e:
    print(e)
    exit(-1)
print("Eigenvalues:\n", np.array2string(L))
print("Eigenvectors:\n", np.array2string(X))
print("Q * Qt =\n", np.array2string(X @ X.T))
print("Q * L * Qt =\n", np.array2string(X @ L @ X.T))