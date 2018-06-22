import math
import numpy as np
a = 7
b = -0.8
c = 0.49
d = 0.17

# def function(X):
#     return X[0]**2 + 2*X[1]**2 - 4*X[0] - 4*X[1]
# def df_x(X):
#     return 2*X[0] - 4
# def df_y(X):
#     return 4*X[1] - 4

def function(X):
    return a*X[0] + b*X[1] + math.e**(c*X[0]**2 + d*X[1]**2)
def df_x(X):
    return a + math.e**(c*X[0]**2 + d*X[1]**2)* 2*c*X[0]
def df_y(X):
    return b + math.e**(c*X[0]**2 + d*X[1]**2)* 2*d*X[1]
def grad(X):
    return np.array([df_x(X), df_y(X)])

def grad_method_shred_step():
    '''Takes function as argument. Returns amount of iterations,
    vector of coordinates of the minimum point, function value in this point.'''

    p = 1
    delta = 0.5
    eps = 0.75
    xy0 = np.array([-1,-1])
    xy = xy0 - p * grad(xy0)
    i = 0
    while (np.linalg.norm(grad(xy)) > np.finfo(np.float32).eps) & (i < 100000):
        if function(xy) <= function(xy0) - eps * p * np.linalg.norm(grad(xy))**2:
            i += 1
            xy0 = xy
            xy = xy0 - p * grad(xy0)
        else:
            p *= delta
            xy = xy0 - p * grad(xy0)
    return i, xy, function(xy)