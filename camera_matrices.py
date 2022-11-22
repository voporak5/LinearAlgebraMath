import math

position = [5,-4,8]
target = [-30,7,8]
up = [-3,10,1]

def sub_vector(v,w):
    x = v[0] - w[0]
    y = v[1] - w[1]
    z = v[2] - w[2]
    return [x,y,z]

def vec_magnitude(v):
    xSquare = v[0] * v[0]
    ySquare = v[1] * v[1]
    zSquare = v[2] * v[2]
    magnitude = math.sqrt(xSquare + ySquare + zSquare)
    return magnitude

def vec_normalize(v):
    magnitude = vec_magnitude(v)
    vNorm = [v[0]/magnitude,v[1]/magnitude,v[2]/magnitude]
    return vNorm

def cross_product(u,v):
    x1 = u[1] * v[2]
    x2 = v[1] * u[2]
    y1 = u[2] * v[0]
    y2 = v[2] * u[0]
    z1 = u[0] * v[1]
    z2 = v[0] * u[1]

    cross = [x1 - x2,y1 - y2,z1 - z2]
    return cross

def matrix_transpose(matrix):
    columns = len(matrix[0])
    rows = len(matrix)
    res = [[0 for x in range(columns)] for y in range(rows)]
    for column in range(columns):
        for row in range(rows):
            res[column][row] = matrix[row][column]
    return res

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

#compute Vdir normalized = Normalize(Tpos-Cpos)
tMinusc = sub_vector(target,position)
vNormalize = vec_normalize(tMinusc)

#compute Cv2w
#vForward norm = -vNormalize
vForward = [-vNormalize[0],-vNormalize[1],-vNormalize[2]]
#compute side
#s = up x vForward
s = cross_product(up,vForward)
vSide = vec_normalize(s)

#compute up
#vUp = vFwd x vSide
vUp = cross_product(vForward,vSide)

cV2W = [[vSide[0],vUp[0],vForward[0],position[0]],
        [vSide[1],vUp[1],vForward[1],position[1]],
        [vSide[2],vUp[2],vForward[2],position[2]],
        [0,0,0,1]]

cV2WRotationMatrix = [[vSide[0],vUp[0],vForward[0]],
                      [vSide[1],vUp[1],vForward[1]],
                      [vSide[2],vUp[2],vForward[2]]]

rTranspose = matrix_transpose(cV2WRotationMatrix)
cInverse = [[-position[0]],[-position[1]],[-position[2]]]

rcInverse = matrix_multiply(rTranspose,cInverse)
rcInverse = [rcInverse[0][0],rcInverse[1][0],rcInverse[2][0]]

cW2V = [[rTranspose[0][0],rTranspose[0][1],rTranspose[0][2],rcInverse[0]],
        [rTranspose[1][0],rTranspose[1][1],rTranspose[1][2],rcInverse[1]],
        [rTranspose[2][0],rTranspose[2][1],rTranspose[2][2],rcInverse[2]],
        [0,0,0,1]]

print("Cv2w")
print(cV2W)

print("Cw2v")
print(cW2V)