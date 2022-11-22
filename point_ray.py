import math

#compute point Q on ray that is closest to Q
q = [0,-6,3]
p0 = [-2,-1,-4]
v = [0,1,-1]

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

def point_ray(q,p0,v):
    qMinusP0 = sub_vector(q,p0)
    vDotQMinusP0 = dot_product(v,qMinusP0)
    vDotv = dot_product(v,v)
    t = vDotQMinusP0/vDotv

    qPrime = 0
    if(t < 0): qPrime = p0
    else: qPrime = add_vector(p0,scale_vector(v,t))

    return qPrime

qPrime = point_ray(q,p0,v)
distance = sub_vector(qPrime,q)
magnitude = vec_magnitude(distance)
print(magnitude)