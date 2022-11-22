import math

#construct rotation to point v towards w
#theta = cos^-1(v dot w / vmag * wmag)
v = [0,3,-4]
w = [-3,5,4]

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

def rodriguez_formula(v,r,theta):
    cosTheta = math.cos(theta)
    minus1Cos = 1 - cosTheta
    sinTheta = math.sin(theta)
    rNorm = vec_normalize(r)
    vDotRNorm = dot_product(v,rNorm)
    minus1CosVDotRNorm = minus1Cos * vDotRNorm
    rNormCrosV = cross_product(rNorm,v)
    rotation = add_vector(add_vector(scale_vector(v,cosTheta),scale_vector(rNorm,minus1CosVDotRNorm)),scale_vector(rNormCrosV,sinTheta))
    return rotation

r = cross_product(v,w)
rNorm = vec_normalize(r)
vdotw = dot_product(v,w)
vMag = vec_magnitude(v)
wMag = vec_magnitude(w)
theta = math.acos(vdotw/(vMag*wMag))
rotation = rodriguez_formula(v,r,theta)

print("r")
print(r)
print("r norm")
print(rNorm)
print("v dot w")
print(vdotw)
print("v mag")
print(vMag)
print("w mag")
print(wMag)
print("theta")
print(theta)
print("rotation")
print(rotation)