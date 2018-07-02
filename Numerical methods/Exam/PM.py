import numpy as np

def PowerMethod(A):
    '''Tekes matrix as argument. Returns maximum absolute
     eigenvalue and it's eigenvector.'''

    delta = 10**(-4)
    y0 = np.ones(len(A))
    lam0 = 1
    x0 = y0 / np.linalg.norm(y0)
    i = 0
    while i < 1000:
        i += 1
        y1 = A @ x0
        x1 = y1 / np.linalg.norm(y0)
        lam1 = y1[abs(x0) > delta] / x0[abs(x0) > delta]
        lam1 = lam1.sum()
        if (lam1 - lam0 < np.finfo('float32').eps):
            break
        x0 = x1
    return lam1, x1