import input_output as io
import gauss

A = io.Input_matrix_from_keyboard()
x = gauss.Gauss(A, [1, 2, 3])
io.print_vector(x, "Answer: ")