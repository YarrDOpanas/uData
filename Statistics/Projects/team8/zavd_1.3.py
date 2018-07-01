import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import scipy.special as ss
from matplotlib import mlab
import pylab

rozpodil = [14.234, 5.336, 4.559, 3.668, 10.839, 9.688,
            7.610, 3.737, 3.276, 11.727, 5.631, 0.664,
            9.050, 7.988, 11.917, 2.719, 1.293, 1.422,
            8.482, 7.471, 3.330, 5.775, 4.336, 3.635,
            3.933, 4.646, 2.144, 8.470, 10.232, 7.172]
rozpodil = sorted(rozpodil)
for i in range(len(rozpodil)):
    print('{:>8}'.format(round(rozpodil[i], 40)), end=' ')
    if (i + 1) % 6 == 0:
        print()
print()

rozpodil_x = []

mean1 = np.mean(rozpodil)
print(mean1)

median1 = np.median(rozpodil)
print(median1)

variance1 = np.var(rozpodil)
print(variance1)

quartile1_1 = np.percentile(rozpodil, 25)
quartile1_2 = np.percentile(rozpodil, 50)
quartile1_3 = np.percentile(rozpodil, 75)
print(quartile1_1, quartile1_2, quartile1_3)
iqr1 = quartile1_3 - quartile1_1
print(iqr1, "\n")

k = 3
tetha = 2

mean2 = k * tetha
print(mean2)

median2 = 5.3481
print(median2)
variance2 = k * tetha * tetha
print(variance2)

m = symbols('m')
x = symbols('x')

fx = integrate(((x ** (k-1)) * exp(-x/tetha)/((tetha ** k) * gamma(k))), (x, m, oo))
#print(fx, "\n")



quartile2_1 = ss.gammaincinv(k, 0.25) * tetha
quartile2_2 = ss.gammaincinv(k, 0.5) * tetha
quartile2_3 = ss.gammaincinv(k, 0.75) * tetha
print(quartile2_1, quartile2_2, quartile2_3)
iqr2 = quartile2_3 - quartile2_1
print(iqr2, "\n")

def delta(a, b):
    return a - b

print(delta(mean1, mean2), delta(median1, median2), delta(variance1, variance2), delta(iqr1, iqr2), "\n")

i1 = mean1 - sqrt(variance1/len(rozpodil)) * np.percentile(rozpodil, 3)
i2 = mean1 + sqrt(variance1/len(rozpodil)) * np.percentile(rozpodil, 3)
print(i1, i2, "\n")

m = 10
v_list = []
def boot(m):
    for i in range(m):
        gamma1 = np.random.gamma(k, tetha, len(rozpodil))
        v_list.append(gamma1.mean())

    boot_mean = np.mean(v_list)

    boot_se = 0
    for i in range(m):
        sum1 = (v_list[i] - boot_mean) ** 2
        boot_se += sum1
    boot_se = sqrt(boot_se/(m-1))

    i2_1 = boot_mean - np.percentile(rozpodil, 3) * boot_se
    i2_2 = boot_mean + np.percentile(rozpodil, 3) * boot_se
    return print(i2_1, i2_2)

boot(10)
boot(100)
boot(1000)

def func (x):
    return ((x ** (k-1)) * exp(-x/tetha)/((tetha ** k) * gamma(k)))

xmin = 0
xmax = 15
dx = 1

xlist = mlab.np.arange (xmin, xmax, dx)

ylist = [func (x) for x in xlist]

pylab.plot (xlist, ylist)
N = len(rozpodil)
width = 1/1.5

pylab.show()

tmp = []
for i in range((round(max(rozpodil))) + 1):
    qwe = 0
    for j in range(len(rozpodil)):
        if rozpodil[j] < (i+1):
            qwe = qwe + 1
    qwe /= len(rozpodil)
    tmp.append(qwe)
print(tmp)

t = symbols('t')
def func_rozp(x1):
    return integrate(((t ** (k-1)) * exp(-t/tetha)/((tetha ** k) * gamma(k))), (t, 0, x1))

x1min = 0
x1max = 15
dx1 = 1

x1list = mlab.np.arange (x1min, x1max, dx1)

y1list = [func_rozp(x1) for x1 in x1list]

pylab.plot (x1list, y1list)
N = len(rozpodil)
width = 1

x = range(len(tmp))
ax = plt.gca()
ax.bar(x, tmp, align='edge') # align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)

pylab.show()
max1 = 0
for x1 in range(len(tmp)):
    tmp1 = abs(func_rozp(x1) - tmp[x1])
    if max1 < tmp1:
        max1 = tmp1
print(max1)