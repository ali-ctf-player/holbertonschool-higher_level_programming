#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in range(len(x)):
            if y + 1  == len(x):
                print("{:d}".format(x[y]), end="")
            else:
                print("{:d}".format(x[y]), end=" ")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
