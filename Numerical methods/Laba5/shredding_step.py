import numpy as np
from scipy import optimize


def grad(X, function):
    return optimize.approx_fprime(X, function, np.finfo(np.float32).eps)

def grad_method_shred_step(function, xy0):
    '''Takes function and initial approximation as argument. Returns amount of iterations,
    vector of coordinates of the minimum point, function value in this point.'''

    p = 1
    delta = 0.5
    eps = 0.75
    xy = xy0 - p * grad(xy0, function)
    i = 0
    while (np.linalg.norm(grad(xy, function)) > 10**(-4)) & (i < 100000):
        if function(xy) <= function(xy0) - eps * p * np.linalg.norm(grad(xy, function))**2:
            i += 1
            xy0 = xy
            xy = xy0 - p * grad(xy0, function)
        else:
            p *= delta
            xy = xy0 - p * grad(xy0, function)
    return i, xy, function(xy)