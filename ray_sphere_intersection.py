import math

c = [12,6,12]
r = 4.5
p0 = [0,2,2]
v = [4,0,3]

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

def sphere_ray_intersect(c,p,v,r):
    cMinusp = sub_vector(c,p)
    vDotCMinusP = dot_product(v,cMinusp)
    vDotv = dot_product(v,v)
    t = vDotCMinusP/vDotv
    #print(t)
    q = 0
    if(t < 0): q = p
    else: q = add_vector(p,scale_vector(v,t))
    
    mag = vec_magnitude(sub_vector(c,q))
    magSquared = mag * mag
    rSquared = r*r

    if(magSquared < rSquared): return True
    else: return False

print(sphere_ray_intersect(c,p0,v,r))