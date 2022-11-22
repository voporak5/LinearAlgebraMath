import math

c = [-12,10,-6]
r = 6

planeP0 = [3,-10,-9]
planeN = [8,7,-1]

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

def sphere_plane_intersection(c,r,p,n):
    cMinusP = sub_vector(c,p)
    cMinusPDotN = dot_product(cMinusP,n)
    nMagnitude = vec_magnitude(n)
    d = abs(cMinusPDotN/nMagnitude)

    if(d < r): return True
    else: return False

print(sphere_plane_intersection(c,r,planeP0,planeN))