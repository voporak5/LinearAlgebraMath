import math

# input two matrices of size n x m
matrix = [[-2,-1,5],
           [-4,5,-4],
           [4,1,3]]

def matrix_transpose(matrix):
    columns = len(matrix[0])
    rows = len(matrix)

    res = [[0 for x in range(columns)] for y in range(rows)]

    for column in range(columns):
        for row in range(rows):
            res[column][row] = matrix[row][column]

    return res

print(matrix_transpose(matrix))