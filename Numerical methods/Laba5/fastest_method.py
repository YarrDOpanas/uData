
import numpy as np
def function(x, y):
    return x**2 - y**2
def df_x(x, y):
    return 2*x
def df_y(x, y):
    return 2*y
def grad(x, y):
    return np.array([df_x(x, y), df_y(x, y)])
def A():
    return np.array([[2,0], [0, -2]])
def F(X):
    return A() @ X @ X/ 2

def gradf(f, x, d):
   df1 = np.empty((d, 1))
   dx = 10**(-3)
   x = x.reshape(d, 1)
   for i in range(d):
       x1 = copy.deepcopy(x)
       x1[i] = x1[i] + dx
       df1[i] = (f(x1)-f(x))/dx
   return df1

def fastest_descent_method():
    '''Takes function as argument. Returns amount of iterations,
    vector of coordinates of the minimum point, function value in this point.'''

    p = 1
    delta = 0.5
    eps = 0.75
    xy0 = np.zeros(2)
    xy = xy0 - p * grad(xy0[0], xy0[1])
    i = 0
    while abs(function(xy[0], xy[1]) - function(xy0[0], xy0[1])) > np.finfo(np.float32).eps:
        p =
        i += 1
        xy0 = xy
        xy = xy0 - p * grad(xy0[0], xy0[1])