import input_output as io
import aditional_functions as af
import simple_iteration_method as SIT
import zaidel

A = io.input_matrix_from_file("matrix.txt")
io.print_matrix(A, "A:")
b = io.input_matrix_from_file("vector.txt")
io.print_matrix(b, "b: ")
af.checking_SLAR(A, b)
x = SIT.simple_iter_method(A, b)
io.print_matrix(x, "Answer via SIT: ")
io.print_matrix(af.subtraction(af.multiplying(A, x), b), "r = A*x - b =")
print("========================")
x = zaidel.zaidel(A, b)
io.print_matrix(x, "Answer via Zaidel: ")
io.print_matrix(af.subtraction(af.multiplying(A, x), b), "r = A*x - b =")
