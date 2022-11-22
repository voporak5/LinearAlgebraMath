import math

obb1Min = [-4.50,-2.50,-3.75]
obb1Max = [5.50,3.50,4.25]

obb2Min = [-4.00,-1.50,-3.50]
obb2Max = [4.00,2.50,4.50]

obb1W = [[-0.212,-0.037,-0.209,-4],
         [0,0.2954,-0.052,-4],
         [0.2121,-0.037,-0.209,3],
         [0,0,0,1]]

obb2W = [[-0.6,-0.412,-0.686,-2],
         [0,0.8575,-0.514,-6],
         [0.8,-0.309,-0.514,9],
         [0,0,0,1]]

#enter a vector from obb_axes_sat
v = [-0.212,0,0.2121]

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

obb1WInverse = getMatrixInverse(obb1W)

#print(obb1WInverse)
v1Prime = matrix_multiply(obb1WInverse,vec_to_matrix(v,0))
v1Prime = matrix_to_vector_3(v1Prime,0)

fwd1 = matrix_to_vector_3(obb1W,2)
s1Squared = dot_product(fwd1,fwd1)

#print(sSquared)

proj1Max = proj_max(obb1Max,obb1Min,v,v1Prime)
proj12 = s1Squared * proj1Max

#print(projMax)
#print(proj12)

obb2WInverse = getMatrixInverse(obb2W)

#print(obb1WInverse)
v2Prime = matrix_multiply(obb2WInverse,vec_to_matrix(v,0))
v2Prime = matrix_to_vector_3(v2Prime,0)

fwd2 = matrix_to_vector_3(obb2W,2)
s2Squared = dot_product(fwd2,fwd2)

#print(sSquared)

proj2Max = proj_max(obb2Max,obb2Min,v,v2Prime)
proj22 = s2Squared * proj2Max

print(proj22)

c1 = scale_vector(add_vector(obb1Max,obb1Min),0.5)
c1 = matrix_multiply(obb1W,vec_to_matrix(c1,1))
c1 = matrix_to_vector_3(c1,0)
print(c1)

c2 = scale_vector(add_vector(obb2Max,obb2Min),0.5)
c2 = matrix_multiply(obb2W,vec_to_matrix(c2,1))
c2 = matrix_to_vector_3(c2,0)

print(c2)

d = abs(dot_product(sub_vector(c2,c1),v))/vec_magnitude(v)
proj1plusproj2 = proj12 + proj22
print(d)
print(proj1plusproj2)

if(d <= proj1plusproj2): print("They intersect")
else: print("they do not intersect")
