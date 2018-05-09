import input_output as io
import gauss
import aditional_functions as af
import LU

A = io.Input_matrix_from_keyboard()
b = io.Input_matrix_from_keyboard()
af.checking_SLAR(A, b)
x = gauss.Gauss(A, b)
if type(x) == int:
    print("The system is degenerate, we figure out it on the " +
          str(-x) + " iteration")
else:
    io.print_matrix(x, "Answer: ")
    io.print_matrix(af.subtraction(af.multiplying(A, x), b), "r = A*x - b = ")
(L, U) = LU.Factorization(A)
if L == False:
    print("This matrix can't be factorized")
    quit(-1)
io.print_matrix(L, "Matrix L:")
io.print_matrix(U, "Matrix U:")
io.print_matrix(af.multiplying(L, U), "L*U = ")
B = LU.Inversed_matrix(L, U)
io.print_matrix(B, "A^(-1) = ")
print("Number of conditionality = " + str(round(LU.matrix_norm(A)*LU.matrix_norm(B), 3)))