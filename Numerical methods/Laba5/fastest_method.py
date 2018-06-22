import numpy as np

def function(X):
    return X[0]**2 + 2*X[1]**2 - 4*X[0] - 4*X[1]
def df_x(X):
    return 2*X[0] - 4
def df_y(X):
    return 4*X[1] - 4
def grad(X):
    return np.array([df_x(X), df_y(X)])
def A():
    return np.array([[2,0], [0,4]])

def fastest_descent_method():
    '''Takes function as argument. Returns amount of iterations,
    vector of coordinates of the minimum point, function value in this point.'''

    xy0 = np.array([-1, -1])
    i = 0
    xy = xy0
    while (np.linalg.norm(grad(xy0))**2 > np.finfo(np.float32).eps) & (i < 100000):
        i += 1
        p = (grad(xy0) @ grad(xy0)) / (A() @ grad(xy0) @ grad(xy0))
        xy = xy0 - p * grad(xy0)
        xy0 = xy
    return i, xy, function(xy)
