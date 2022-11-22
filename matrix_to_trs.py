import math

#enter the matrix
matrix = [[0,2,3,1],
          [-5,-5,-3,2],
          [5,-3,1,3],
          [0,0,0,1]]

t = [[1,0,0,matrix[0][3]],
    [0,1,0,matrix[1][3]],
    [0,0,1,matrix[2][3]],
    [0,0,0,1]]

magx = math.sqrt((matrix[0][0] * matrix[0][0]) + (matrix[1][0] * matrix[1][0]) + (matrix[2][0] * matrix[2][0]))
magy = math.sqrt((matrix[0][1] * matrix[0][1]) + (matrix[1][1] * matrix[1][1]) + (matrix[2][1] * matrix[2][1]))
magz = math.sqrt((matrix[0][2] * matrix[0][2]) + (matrix[1][2] * matrix[1][2]) + (matrix[2][2] * matrix[2][2]))

s = [[magx,0,0,0],
    [0,magy,0,0],
    [0,0,magz,0],
    [0,0,0,1]]



r = [[matrix[0][0]/magx,matrix[0][1]/magy,matrix[0][2]/magz,0],
    [matrix[1][0]/magx,matrix[1][1]/magy,matrix[1][2]/magz,0],
    [matrix[2][0]/magx,matrix[2][1]/magy,matrix[2][2]/magz,0],
    [0,0,0,1]]

print("t")
print(t)

print("r")
print(r)

print("s")
print(s)