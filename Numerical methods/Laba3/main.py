import numpy as np
import Jacobi
import QR

np.set_printoptions(precision=3)

try:
    A = np.loadtxt("matrix.txt")
except(Exception):
    print("Could not find file or invalid matrix")
    exit(-1)
print("Our matrix:")
print(A)
# try:
#     L, X = Jacobi.Jacobi(A)
# except Exception as e:
#     print(e)
#     exit(-1)
# print("Eigenvalues:\n", np.array2string(L))
# print("Eigenvectors:\n", np.array2string(X))
# print("Q * Qt =\n", np.array2string(X @ X.T))
# print("Q * L * Qt =\n", np.array2string(X @ L @ X.T))
# A = np.random.random(16).reshape(4, 4)

R = QR.QR(A)
print("Result matrix:\n" + np.array2string(R))
print("Answer via numpy: " + np.array2string(np.linalg.eigvals(A)))
