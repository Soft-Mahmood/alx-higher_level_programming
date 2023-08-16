#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	matrix2 = []
	for rom in matrix:
		row2 = list([x**2 for x in rom])
		matrix2.append(row2)
	return matrix2
