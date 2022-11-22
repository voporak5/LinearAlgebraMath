import math

# input two matrices of size n x m
matrix1 = [[4,-2,2],
           [3,1,-5],
           [-3,0,4]]

matrix2 = [[5,3,0],
           [-3,3,-4],
           [3,-1,1]]
 
def matrix_multiply(matrix1,matrix2):

    matrix1Columns = len(matrix1[0])
    matrix2Rows = len(matrix2)

    res = [[0 for x in range(matrix1Columns)] for y in range(matrix2Rows)]
    
    # explicit for loops
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
    
                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res
 
print (matrix_multiply(matrix1,matrix2))