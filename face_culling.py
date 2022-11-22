import math

vertices = [[0,1,0,1],[0,0,2,1],[-1,0,-1,1],[1,0,-1,1]]
red = [1,2,4]
blue = [1,4,3]
green = [1,3,2]
white = [2,3,4]

tgoMatrix = [[-0.9976,-0.0121,0.0687,1],
             [0,0.9848,0.1736,0],
             [-0.0698,0.1732,-0.9824,2],
             [0,0,0,1]]

cPos = [-5,5,5]
cTarg = [1,0,2]
up = [0,1,0]

redEnabled = 1
blueEnabled = 0
greenEnabled = 0
whiteEnabled = 0

def vec_to_matrix(v,w):
    matrix = [[v[0]],[v[1]],[v[2]],[w]]
    return matrix

def sub_vector(v,w):
    x = v[0] - w[0]
    y = v[1] - w[1]
    z = v[2] - w[2]
    return [x,y,z]

def cross_product(u,v):
    x1 = u[1] * v[2]
    x2 = v[1] * u[2]
    y1 = u[2] * v[0]
    y2 = v[2] * u[0]
    z1 = u[0] * v[1]
    z2 = v[0] * u[1]

    cross = [x1 - x2,y1 - y2,z1 - z2]
    return cross

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

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

def cull_face(matrix,vertices,order,cPos):
    aVerts = vertices[order[0]-1]
    a = matrix_multiply(matrix,vec_to_matrix(aVerts,aVerts[3]))
    a = [a[0][0],a[1][0],a[2][0],a[3][0]]

    bVerts = vertices[order[1]-1]
    b = matrix_multiply(matrix,vec_to_matrix(bVerts,bVerts[3]))
    b = [b[0][0],b[1][0],b[2][0],b[3][0]]

    cVerts = vertices[order[2]-1]
    c = matrix_multiply(matrix,vec_to_matrix(cVerts,cVerts[3]))
    c = [c[0][0],c[1][0],c[2][0],c[3][0]]

    v1 = sub_vector(b,a)   
    v2 = sub_vector(c,a)
    n = cross_product(v1,v2)
    vLos = sub_vector(a,cPos)
    dot = dot_product(vLos,n)

    if(dot < 0): return False
    else: return True

if(redEnabled == 1): print(cull_face(tgoMatrix,vertices,red,cPos))
if(blueEnabled == 1): print(cull_face(tgoMatrix,vertices,blue,cPos))
if(greenEnabled == 1): print(cull_face(tgoMatrix,vertices,green,cPos))
if(whiteEnabled == 1): print(cull_face(tgoMatrix,vertices,white,cPos))