import numpy as np
import PM
np.set_printoptions(precision=3)

try:
    A = np.loadtxt("matrix.txt")
    b = np.loadtxt("vector.txt")
except(Exception):
    print("Could not find file or invalid matrix")
    exit(-1)

print("Our matrix:\n", A)
print("Our vector:", b)
lam, x = PM.PowerMethod(A)
print("Max absolute eigenvalue: ", lam)
print("It's eigenvector: ", x)
# U, E, V = np.linalg.svd(A)
# print("Via numpy: ", E[0])
# print()