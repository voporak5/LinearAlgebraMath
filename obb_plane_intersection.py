import math

minX = float(input("minX: "))
minY = float(input("minY: "))
minZ = float(input("minZ: "))

maxX = float(input("maxX: "))
maxY = float(input("maxY: "))
maxZ = float(input("maxZ: "))

obbMin = [minX,minY,minZ]#input("obbm: ")#[-1.5,-3.5,-4.375]
obbMax = [maxX,maxY,maxZ]

def getMatrix():
    print("enter matrix")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    x3 = float(input("x3: "))
    y1 = float(input("y1: "))
    y2 = float(input("y2: "))
    y3 = float(input("y3: "))
    z1 = float(input("z1: "))
    z2 = float(input("z2: "))
    z3 = float(input("z3: "))
    p1 = float(input("p1: "))
    p2 = float(input("p2: "))
    p3 = float(input("p3: "))
    return [[x1,y1,z1,p1],
            [x2,y2,z2,p2],
            [x3,y3,z3,p3],
            [0,0,0,1]]

obbW = getMatrix()#[[-0.4386,-0.0872,-0.8944,-13],
         #[-0.1949,0.98081,0,0],
        # [0.87727,0.17437,-0.4472,-7],
         #[0,0,0,1]]

planeP0X = float(input("planeP0X: "))
planeP0Y = float(input("planeP0Y: "))
planeP0Z = float(input("planeP0Z: "))

planeNX = float(input("planeNX: "))
planeNY = float(input("planeNY: "))
planeNZ = float(input("planeNZ: "))

planeP0 = [planeP0X,planeP0Y,planeP0Z]
planeN = [planeNX,planeNY,planeNZ]

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

def matrix_transpose(matrix):
    columns = len(matrix[0])
    rows = len(matrix)
    res = [[0 for x in range(columns)] for y in range(rows)]
    for column in range(columns):
        for row in range(rows):
            res[column][row] = matrix[row][column]
    return res
	
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
	
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
	
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)  

    cofactors = matrix_transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def matrix_to_vector_3(m,c):
    return [m[0][c],m[1][c],m[2][c]]

def matrix_to_vector_4(m,c):
    return [m[0][c],m[1][c],m[2][c],m[3][c]]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    return [x,y,z]

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

def proj_max(max,min,v,vPrime):
    d = scale_vector(sub_vector(max,min),0.5)
    a = d[0]
    b = d[1]
    c = d[2]
    vMagnitude = vec_magnitude(v)
    projMax = (abs(a*vPrime[0]) + abs(b*vPrime[1]) + abs(c*vPrime[2])) / vMagnitude
    return projMax

def add_vector(v,w):
    x = v[0] + w[0]
    y = v[1] + w[1]
    z = v[2] + w[2]
    return [x,y,z]

obbWInverse = getMatrixInverse(obbW)

print("obb inverse")
print(obbWInverse)
vPrime = matrix_multiply(obbWInverse,vec_to_matrix(planeN,0))
vPrime = matrix_to_vector_3(vPrime,0)

print("v prime")
print(vPrime)

fwd = matrix_to_vector_3(obbW,2)
sSquared = dot_product(fwd,fwd)

print("s squared")
print(sSquared)

#print(sSquared)

projMax = proj_max(obbMax,obbMin,planeN,vPrime)
proj2 = sSquared * projMax

print("proj max")
print(projMax)
print("proj2")
print(proj2)

c = scale_vector(add_vector(obbMax,obbMin),0.5)
c = matrix_multiply(obbW,vec_to_matrix(c,1))
c = matrix_to_vector_3(c,0)
print("c")
print(c)
print("h")
h = proj2

nMagnitude = vec_magnitude(planeN)
s1 = sub_vector(c,scale_vector(scale_vector(planeN,1/nMagnitude),h))
s2 = add_vector(c,scale_vector(scale_vector(planeN,1/nMagnitude),h))
d1 = dot_product(sub_vector(s1,planeP0),planeN)
d2 = dot_product(sub_vector(s2,planeP0),planeN)

print("s1")
print(s1)
print("s2")
print(s2)

print("d1")
print(d1)
print("d2")
print(d2)

if(d1 > 0): print("obb above plane d1 > 0")
elif(d2 < 0): print("obb below plane d2 < 0")
else: print("obb intersects plane d1 < 0, d2 > 0 ")