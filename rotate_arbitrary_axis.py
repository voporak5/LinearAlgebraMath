import math

#axis to rotate around x,y,z
r = [-1,-3,-4]
#vector being rotated
v = [-4,5,-4]

#degrees to rotate by
theta = (-math.pi * 4) / 8


def vec_normalize(v):
    xSquare = v[0] * v[0]
    ySquare = v[1] * v[1]
    zSquare = v[2] * v[2]
    magnitude = math.sqrt(xSquare + ySquare + zSquare)
    vNorm = [v[0]/magnitude,v[1]/magnitude,v[2]/magnitude]
    return vNorm

def vec_to_matrix(v):
    matrix = [[v[0]],[v[1]],[v[2]],[0]]
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

rNorm = vec_normalize(r)
c = math.cos(theta)
s = math.sin(theta)
t = 1 - c



rMatrix = [[t*rNorm[0]*rNorm[0]+c,t*rNorm[0]*rNorm[1]-s*rNorm[2],t*rNorm[0]*rNorm[2]+s*rNorm[1],0],
          [t*rNorm[0]*rNorm[1]+s*rNorm[2],t*rNorm[1]*rNorm[1]+c,t*rNorm[1]*rNorm[2]-s*rNorm[0],0],
          [t*rNorm[0]*rNorm[2]-s*rNorm[1],t*rNorm[1]*rNorm[2]+s*rNorm[0],t*rNorm[2]*rNorm[2]+c,0],
          [0,0,0,1]]

print("r norm")
print(rNorm)
print("c")
print(c)
print("s")
print(s)
print("t")
print(t)
print("r matrix")
print(rMatrix)
print("new vector")
vAsMatrix = vec_to_matrix(v)
print(matrix_multiply(rMatrix,vAsMatrix))