#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        for i in index:
            print("{:d}".format(i), end="")
        print(end='\n')
