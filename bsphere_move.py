import math

c = [-0.13,0.125,0]
r = 1.5

w = [[0.915,-0.24,0.324,10],
     [0.4,0.427,-0.81,7],
     [0.057,0.872,0.487,4],
     [0,0,0,1]]

def vec_to_matrix(v,w):
    matrix = [[v[0]],[v[1]],[v[2]],[w]]
    return matrix

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

def vec_magnitude(v):
    xSquare = v[0] * v[0]
    ySquare = v[1] * v[1]
    zSquare = v[2] * v[2]
    magnitude = math.sqrt(xSquare + ySquare + zSquare)
    return magnitude

def sphere_world_pos(w,c):
    cPrime = matrix_multiply(w,vec_to_matrix(c,1))
    cPrime = [cPrime[0][0],cPrime[1][0],cPrime[2][0],cPrime[3][0]]
    return cPrime

def sphere_world_radius(w,r):
    vSide = [w[0][0],w[1][0],w[2][0]]
    a = vec_magnitude(vSide)
    rPrime = a * r
    return rPrime

print(sphere_world_pos(w,c))
print(sphere_world_radius(w,r))