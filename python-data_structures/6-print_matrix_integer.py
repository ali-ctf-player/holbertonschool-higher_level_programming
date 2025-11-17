#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in range(len(x)):
            if y + 1 == len(x):
                print("{:d}".format(x[y]), end="")
            else:
                print("{:d}".format(x[y]), end=" ")
        print()
