#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for x in range(len(matrix)):
        for y in range(len(x)):
            matrix[x][y] = matrix[y] ** 2
    return matrix
