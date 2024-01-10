#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            squared_x = x ** 2
            new_row.append(squared_x)
        new_matrix.append(new_row)

    return new_matrix
