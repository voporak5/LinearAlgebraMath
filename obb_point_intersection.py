import math

obbMin = [-1.25,-1,-0.5]
obbMax = [1.75,1,1.5]

w = [[1,0,0,10],
     [0,1,0,0],
     [0,0,1,-10],
     [0,0,0,1]]

p = [15.25,0,-6.5]

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

def vec_to_matrix(v,w):
    matrix = [[v[0]],[v[1]],[v[2]],[w]]
    return matrix

def point_in_range(p,min,max):
    if(p > min and p < max): return True
    else: return False

def point_in_obb(m,p,min,max):
    mInverse = getMatrixInverse(m)
    pPrime = matrix_multiply(mInverse,vec_to_matrix(p,1))
    pPrime =[pPrime[0][0],pPrime[1][0],pPrime[2][0],pPrime[3][0]]

    xInside = point_in_range(pPrime[0],min[0],max[0])
    yInside = point_in_range(pPrime[1],min[1],max[1])
    zInside = point_in_range(pPrime[2],min[2],max[2])

    if(xInside == True and yInside == True and zInside == True): return True
    else: return False

print(point_in_obb(w,p,obbMin,obbMax))