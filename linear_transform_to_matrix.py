import math

#T(v)=(v . n)n

n = [1,-2,3]

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    return [x,y,z]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

x = scale_vector(n,dot_product([1,0,0],n))
y = scale_vector(n,dot_product([0,1,0],n))
z = scale_vector(n,dot_product([0,0,1],n))

print([x,y,z])