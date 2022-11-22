import math

lineP0 = [6,0,3]
lineV = [-4,0,-3]

aabbMin = [3,-1,-0.5]
aabbMax = [9,1,6.5]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

def vec_magnitude(v):
    xSquare = v[0] * v[0]
    ySquare = v[1] * v[1]
    zSquare = v[2] * v[2]
    magnitude = math.sqrt(xSquare + ySquare + zSquare)
    return magnitude

def sub_vector(v,w):
    x = v[0] - w[0]
    y = v[1] - w[1]
    z = v[2] - w[2]
    return [x,y,z]

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    return [x,y,z]

def add_vector(v,w):
    x = v[0] + w[0]
    y = v[1] + w[1]
    z = v[2] + w[2]
    return [x,y,z]

def min_max_overlap(min,max,p,v):
    a = 0
    b = 0
    if(v != 0): 
        a = (min - p) / v
        b = (max - p) / v

    left = 0
    right = 0
    if(a < b): 
        left = a
        right = b
    else:
        left = b
        right = a
    
    return [left,right]

def interval_overlap(min1,min2,max1,max2):
    max1min2 = max1 < min2
    max2min1 = max2 < min1

    if(max1min2 == False and max2min1 == False): return True
    else: return False

if(lineV[0] == 0):
    if(lineP0[0] < aabbMin[0] or lineP0[0] > aabbMax[0]): 
        print("no intersection")
    else:
        print("al the axis is covered")
else:

    sXtX = min_max_overlap(aabbMin[0],aabbMax[0],lineP0[0],lineV[0])
    sYtY = min_max_overlap(aabbMin[1],aabbMax[1],lineP0[1],lineV[1])
    sZtZ = min_max_overlap(aabbMin[2],aabbMax[2],lineP0[2],lineV[2])

    xy = interval_overlap(sXtX[0],sYtY[0],sXtX[1],sYtY[1])
    yz = interval_overlap(sYtY[0],sZtZ[0],sYtY[1],sZtZ[1])
    zx = interval_overlap(sZtZ[0],sXtX[0],sZtZ[1],sXtX[1])

    if(xy and yz and zx): print("line and aabb intersect")
    else: print("they do not intersect")
