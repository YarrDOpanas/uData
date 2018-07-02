import numpy as np
import PM
np.set_printoptions(precision=3)

# try:
#     A = np.loadtxt("ex_m.txt")
#     b = np.loadtxt("vector.txt")
# except(Exception):
#     print("Could not find file or invalid matrix")
#     exit(-1)

A = np.array([[0,1,0], [-4,4,0], [-2,1,2]])

print("Our matrix:\n", A)
# print("Our vector:", b)
lam, x = PM.PowerMethod(A)
print("Max absolute eigenvalue: ", lam)
print("It's eigenvector: ", x)
# w, v = np.linalg.eig(A)
# print("-----------------------")
# print("Via numpy:\nEigenvalues:", w)
# print("Eigenvectors\n", v)