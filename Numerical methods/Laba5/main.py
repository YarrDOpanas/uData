import shredding_step as sh_step
import fastest_method as f_method
import numpy as np
import math
from scipy import optimize
np.set_printoptions(precision=3)
a = 7
b = -0.8
c = 0.49
d = 0.17

def f1(X):
    return a*X[0] + b*X[1] + math.e**(c*X[0]**2 + d*X[1]**2)

# def f1(X):
#     return (X[0] ** 2 - 2) / (1 + X[0]**4)

# def f2(X):
#     return X[0]**2 + 2*X[1]**2 - 4*X[0] - 4*X[1]

def f2(X):
    return X[0]**2 + X[1]**2

i, xy, f = sh_step.grad_method_shred_step(f1, np.array([1, 1]))
print("Shredding steps:")
print("Point: ", xy)
print("F = ", round(f,3))
print("Amount of iterations: ", i)
print("\nVia pythons library:")
print(optimize.fmin(f1, np.array([1,1])))
print("-------------------------")
f_method.partial_derivative()
i, xy, f = f_method.fastest_descent_method(f2, np.array([3, 2]))
print("Fastest descent method(for quadratic forms):")
print("Point: ", xy)
print("F = ", round(f,3))
print("Amount of iterations: ", i)
print("\nVia pythons library:")
print(optimize.fmin(f2, np.array([3,2])))