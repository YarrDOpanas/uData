import shredding_step as sh_step
import fastest_method as f_method
import numpy as np
np.set_printoptions(precision=3)

i, xy, f = sh_step.grad_method_shred_step()
print("Shredding steps:")
print("Point: ", xy)
print("F(x, y) = ", round(f,3))
print("Amount of iterations: ", i)
print("-------------------------")
i, xy, f = f_method.fastest_descent_method()
print("Fastest descent method(for quadratic forms):")
print("Point: ", xy)
print("F(x, y) = ", round(f,3))
print("Amount of iterations: ", i)