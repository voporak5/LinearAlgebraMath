import math
u = [0,1,2]
v = [0,1,2]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

print(dot_product(u,v))