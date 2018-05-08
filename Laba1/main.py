import input_output as io
import gauss
import aditional_functions as af

A = io.Input_matrix_from_keyboard()
b = io.Input_matrix_from_keyboard()
x = gauss.Gauss(A, b)
if type(x) == int:
    print("The system is degenerate, we figure out it on the " +
          str(-x) + " iteration")
else:
    io.print_matrix(x, "Answer: ")
    io.print_matrix(af.subtraction(af.multiplying(A, x), b), "r = A*x - b = ")