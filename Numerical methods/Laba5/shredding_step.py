import numpy as np
import math

a = 7
b = -0.8
c = 0.49
d = 0.17
def function(x, y):
    return a*x + b*y + math.e**(c*x**2 + d*y**2)
def df_x(x, y):
    return a + math.e**(c*x**2 + d*y**2)* 2*c*x
def df_y(x, y):
    return b + math.e**(c*x**2 + d*y**2)* 2*d*y
def grad(x, y):
    return np.array([df_x(x, y), df_y(x, y)])

def grad_method_shred_step():
    '''Takes function as argument. Returns amount of iterations,
    vector of coordinates of the minimum point, function value in this point.'''

    p = 1
    delta = 0.5
    eps = 0.75
    xy0 = np.zeros(2)
    xy = xy0 - p * grad(xy0[0], xy0[1])
    i = 0
    while np.linalg.norm(grad(xy[0], xy[1])) > np.finfo(np.float32).eps:
        while function(xy[0], xy[1]) <= function(xy0[0], xy0[1]) - eps * p * np.linalg.norm(grad(xy[0], xy[1]))**2:
            i += 1
            xy0 = xy
            xy = xy0 - p * grad(xy0[0], xy0[1])
        p *= delta
        xy = xy0 - p * grad(xy0[0], xy0[1])
    return i, xy, function(xy[0], xy[1])