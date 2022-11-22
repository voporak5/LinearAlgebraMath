import math

position = [550,0,700]
target = [450,0,1100]
up = [0,1,0]

point1 = [540,7.5,850,1]
point2 = [450,7.5,1100,1]
point3 = [250,7.5,1300,1]

fieldOfView = 1*math.pi/8
nearClip = 100
farClip = 700
ndc = [-1,1]
aspect = 1.7778
width = 1280
height = 720
zDepth = [0,1]

mouseX = 300
mouseY = 150

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
    
def vec_to_matrix(v,w):
    matrix = [[v[0]],[v[1]],[v[2]],[w]]
    return matrix

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    w = v[3] * s
    return [x,y,z,w]

def camera_view_to_world(target,position,up):
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

    return cV2W
    
def camera_world_to_view(position,worldToViewMatrix):
    cV2WRotationMatrix = [[worldToViewMatrix[0][0],worldToViewMatrix[0][1],worldToViewMatrix[0][2]],
                          [worldToViewMatrix[1][0],worldToViewMatrix[1][1],worldToViewMatrix[1][2]],
                          [worldToViewMatrix[2][0],worldToViewMatrix[2][1],worldToViewMatrix[2][2]]]

    rTranspose = matrix_transpose(cV2WRotationMatrix)
    cInverse = [[-position[0]],[-position[1]],[-position[2]]]
    
    rcInverse = matrix_multiply(rTranspose,cInverse)
    rcInverse = [rcInverse[0][0],rcInverse[1][0],rcInverse[2][0]]

    cW2V = [[rTranspose[0][0],rTranspose[0][1],rTranspose[0][2],rcInverse[0]],
            [rTranspose[1][0],rTranspose[1][1],rTranspose[1][2],rcInverse[1]],
            [rTranspose[2][0],rTranspose[2][1],rTranspose[2][2],rcInverse[2]],
            [0,0,0,1]]

    return cW2V

def persp_matrix(n,f,a,t):
    halfT = t/2;
    d = math.cos(halfT)/math.sin(halfT)
    x = d/a
    y = d
    z = -(f+n)/(f - n)
    px = 0
    py = 0
    pz = (-2*f*n)/(f - n)
    matrix = [[x,0,0,px],
              [0,y,0,py],
              [0,0,z,pz],
              [0,0,-1,0]]
    return matrix

def ndc_to_scr_matrix(width,height,zDepth):
    zRange = zDepth[1] - zDepth[0]
    x = width / 2
    y = -height / 2
    z = zRange / 2
    matrix = [[x,0,0,x],
              [0,y,0,-y],
              [0,0,z,z],
              [0,0,0,1]]
    return matrix

def scr_to_ndc_matrix(width,height,zDepth):
    zRange = zDepth[1] - zDepth[0]
    x = 2 / width
    y = -2 / height
    z = 2 / zRange
    matrix = [[x,0,0,-1],
              [0,y,0,1],
              [0,0,z,-1],
              [0,0,0,1]]
    return matrix

def inverse_persp_matrix(n,f,a,t):
    halfT = t/2;
    d = math.cos(halfT)/math.sin(halfT)
    x = a/d
    y = 1/d
    z = -(f-n)/(2*f*n)
    px = 0
    py = 0
    pz = (f+n)/(2*f*n)
    matrix = [[x,0,0,px],
              [0,y,0,py],
              [0,0,0,-1],
              [0,0,z,pz]]
    return matrix

cV2W = camera_view_to_world(target,position,up)
cW2V = camera_world_to_view(position,cV2W)

point1ToView = matrix_multiply(cW2V,vec_to_matrix(point1,1))
point1ToView = [point1ToView[0][0],point1ToView[1][0],point1ToView[2][0],point1ToView[3][0]]

point2ToView = matrix_multiply(cW2V,vec_to_matrix(point2,1))
point2ToView = [point2ToView[0][0],point2ToView[1][0],point2ToView[2][0],point2ToView[3][0]]

point3ToView = matrix_multiply(cW2V,vec_to_matrix(point3,1))
point3ToView = [point3ToView[0][0],point3ToView[1][0],point3ToView[2][0],point3ToView[3][0]]

mPersp = persp_matrix(nearClip,farClip,aspect,fieldOfView)
#print(point1ToView)
#print(point2ToView)
#print(point3ToView)
#print(mPersp)

point1ToPersp = matrix_multiply(mPersp,vec_to_matrix(point1ToView,1))
point1ToPersp = [point1ToPersp[0][0],point1ToPersp[1][0],point1ToPersp[2][0],point1ToPersp[3][0]]
point1ToPersp = scale_vector(point1ToPersp,1/point1ToPersp[3])

point2ToPersp = matrix_multiply(mPersp,vec_to_matrix(point2ToView,1))
point2ToPersp = [point2ToPersp[0][0],point2ToPersp[1][0],point2ToPersp[2][0],point2ToPersp[3][0]]
point2ToPersp = scale_vector(point2ToPersp,1/point2ToPersp[3])

point3ToPersp = matrix_multiply(mPersp,vec_to_matrix(point3ToView,1))
point3ToPersp = [point3ToPersp[0][0],point3ToPersp[1][0],point3ToPersp[2][0],point3ToPersp[3][0]]
point3ToPersp = scale_vector(point3ToPersp,1/point3ToPersp[3])

#check if inside ndc
#print(point1ToPersp)
#print(point2ToPersp)
#print(point3ToPersp)

mNdcToScr = ndc_to_scr_matrix(width,height,zDepth)
#print(mNdcToScr)

point1ToScr = matrix_multiply(mNdcToScr,vec_to_matrix(point1ToPersp,1))
point1ToScr = [point1ToScr[0][0],point1ToScr[1][0],point1ToScr[2][0],point1ToScr[3][0]]

point2ToScr = matrix_multiply(mNdcToScr,vec_to_matrix(point2ToPersp,1))
point2ToScr = [point2ToScr[0][0],point2ToScr[1][0],point2ToScr[2][0],point2ToScr[3][0]]

point3ToScr = matrix_multiply(mNdcToScr,vec_to_matrix(point3ToPersp,1))
point3ToScr = [point3ToScr[0][0],point3ToScr[1][0],point3ToScr[2][0],point3ToScr[3][0]]

#check if in xy frame and z depth
#print(point1ToScr)
#print(point2ToScr)
#print(point3ToScr)

near = [mouseX,mouseY,0,1]
far = [mouseX,mouseY,zDepth[1] - zDepth[0],1]

mScrToNdc = scr_to_ndc_matrix(width,height,zDepth)

ndcNear = matrix_multiply(mScrToNdc,vec_to_matrix(near,1))
ndcNear = [ndcNear[0][0],ndcNear[1][0],ndcNear[2][0],ndcNear[3][0]]

ndcFar = matrix_multiply(mScrToNdc,vec_to_matrix(far,1))
ndcFar = [ndcFar[0][0],ndcFar[1][0],ndcFar[2][0],ndcFar[3][0]]

#print(ndcNear)
#print(ndcFar)

inversePersp = inverse_persp_matrix(nearClip,farClip,aspect,fieldOfView)

homNear = matrix_multiply(inversePersp,vec_to_matrix(ndcNear,1))
homNear = [homNear[0][0],homNear[1][0],homNear[2][0],homNear[3][0]]

homFar = matrix_multiply(inversePersp,vec_to_matrix(ndcFar,1))
homFar = [homFar[0][0],homFar[1][0],homFar[2][0],homFar[3][0]]

camNear = scale_vector(homNear,nearClip)
camFar = scale_vector(homFar,farClip)

#print(camNear)
#print(camFar)

worldNear = matrix_multiply(cV2W,vec_to_matrix(camNear,1))
worldNear = [worldNear[0][0],worldNear[1][0],worldNear[2][0],worldNear[3][0]]

worldFar = matrix_multiply(cV2W,vec_to_matrix(camFar,1))
worldFar = [worldFar[0][0],worldFar[1][0],worldFar[2][0],worldFar[3][0]]

print(worldNear)
print(worldFar)