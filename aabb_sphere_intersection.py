import math

aabb1Min = [3.5,-1,-6.5]
aabb1Max = [8.5,1,-1.5]

c = [-9,0,7]
r = 2.5

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

def clamp_point(p,min,max):

    pPrime = [0,0,0]

    if(p[0] < min[0]): pPrime[0] = min[0]
    elif(p[0] > max[0]): pPrime[0] = max[0]
    else: pPrime[0] = p[0]

    if(p[1] < min[1]): pPrime[1] = min[1]
    elif(p[1] > max[1]): pPrime[1] = max[1]
    else: pPrime[1] = p[1]

    if(p[2] < min[2]): pPrime[2] = min[2]
    elif(p[2] > max[2]): pPrime[2] = max[2]
    else: pPrime[2] = p[2]

    return pPrime

def point_in_sphere(min,max,c,r):
    cClamped = clamp_point(c,min,max)
    cClampedMinusC = sub_vector(cClamped,c)
    magnitude = vec_magnitude(cClampedMinusC)

    if(magnitude < r): return True
    else: return False

print(point_in_sphere(aabb1Min,aabb1Max,c,r))