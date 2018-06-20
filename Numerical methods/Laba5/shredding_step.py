import numpy as np
import math

a = 7
b = -0.8
c = 0.49
d = 0.17
def function(X):
    return a*X[0] + b*X[1] + math.e**(c*X[0]**2 + d*X[1]**2)

def grad_method_shred_step(f):
    '''Takes function as argument. Returns minimum
    of this function.'''

    p0 = 1
    delta = 0.5
    eps = 0.75
    xo = np.zeros(2)
    grad = np.gradient(function(x0))
