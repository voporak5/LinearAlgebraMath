#reflect v through plane with normal n
n = [1,3,-2]
v = [-3,0,1]

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

scale = 2 * (dot_product(v,n)/dot_product(n,n))
dif = sub_vector(v,scale_vector(n,scale))
reflection = [dif[0],dif[1],dif[2],0]
print(reflection)
