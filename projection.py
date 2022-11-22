import math

#projection of v onto w
v = [1,1,-1]
w = [-1,1,4]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    return [x,y,z]

def sub_vector(v,w):
    x = v[0] - w[0]
    y = v[1] - w[1]
    z = v[2] - w[2]
    return [x,y,z]

vDotw = dot_product(v,w)
wDotw = dot_product(w,w)
vDotwDividedwDotw = vDotw/wDotw
projVtoW = scale_vector(w,vDotwDividedwDotw);
perpVtoW = sub_vector(v,projVtoW)

print("Projection")
print(projVtoW)

print("Perpendicular")
print(perpVtoW)