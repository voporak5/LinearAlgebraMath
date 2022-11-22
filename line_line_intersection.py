import math

line1P0 = [-3,0,4]
line1V = [-3,0,5]

line2P0 = [-1,-1,3]
line2V = [1,-4,-3]

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

a = dot_product(line1V,line1V)
b = dot_product(line1V,line2V)
c = dot_product(line2V,line2V)
d = dot_product(sub_vector(line1P0,line2P0),line1V)
e = dot_product(sub_vector(line1P0,line2P0),line2V)

parallelCheck = b*b - a*c
c1 = line1P0
c2 = line2P0 + scale_vector(line2V,e/c)

if(parallelCheck == 0):
    print("parallel lines")
else:
    print("not parallel")
    c1 = add_vector(line1P0, scale_vector(line1V,((c*d - b*e)/(b*b - a*c))))
    c2 = add_vector(line2P0, scale_vector(line2V,((d*b - a*e)/(b*b - a*c))))

print(c1)
print(c2)
distance = vec_magnitude(sub_vector(c1,c2))
print(distance)