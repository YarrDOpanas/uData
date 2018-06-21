import shredding_step as sh_step

i, xy, f = sh_step.grad_method_shred_step()
print("Vecor: ", xy)
print("F(x) = ", f)
print("Amount of iterations: ", i)