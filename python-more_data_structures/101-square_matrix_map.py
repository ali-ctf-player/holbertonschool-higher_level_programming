#!/usr/bin/python3

def square_matrix_map(matrix):
    new_matrix = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return new_matrix
