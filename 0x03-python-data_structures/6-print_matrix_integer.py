#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in matrix[row]:
            print("{}".format(i), end=" ")
        print()
