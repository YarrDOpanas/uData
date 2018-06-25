import numpy as np
from sympy import symbols, Derivative
from scipy import optimize

def grad(X, function):
    return optimize.approx_fprime(X, function, np.finfo(np.float32).eps)

def A():
    return np.array([[2,0], [0,2]])

def partial_derivative():
    x, y = symbols('x y')
    f = x ** 2 + 2 * y ** 2 - 4 * x - 4 * y
    print("Our function: ", f)
    print("df/dx = ", Derivative(f, x).doit())
    print("df/dy = ", Derivative(f, y).doit())

def fastest_descent_method(function, xy0):
    '''Takes function and initial approximation as argument. Returns amount of iterations,
    vector of coordinates of the minimum point, function value in this point.'''
    i = 0
    xy = xy0
    while (np.linalg.norm(grad(xy0, function))**2 > np.finfo(np.float32).eps) & (i < 100000):
        i += 1
        p = (grad(xy0, function) @ grad(xy0, function)) / (A() @ grad(xy0, function) @ grad(xy0, function))
        xy = xy0 - p * grad(xy0, function)
        xy0 = xy
    return i, xy, function(xy)
