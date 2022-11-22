segment = [[-8,0,-6],
           [6,-1,-1]]

planeP = [2,7,10]
planeN = [9,7,7]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]

    dot = x + y + z;
    return dot

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

s1 = segment[0]
s2 = segment[1]
pMinusS1 = sub_vector(planeP,s1)
s2MinusS1 = sub_vector(s2,s1)

t = dot_product(pMinusS1,planeN)/dot_product(s2MinusS1,planeN)

if(t < 0 or t > 1): print("no intersection")
else:
    q = add_vector(s1,scale_vector(s2MinusS1,t))
    print("intersection at")
    print(t)