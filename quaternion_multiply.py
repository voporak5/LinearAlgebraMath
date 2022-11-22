
#multiply two quaternions
#q = [w,v]
q1 = [0.981,-0.185,0,0.062]
q2 = [2,0,-2,3]

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

v1 = [q1[1],q1[2],q1[3]]
v2 = [q2[1],q2[2],q2[3]]
w1 = q1[0]
w2 = q2[0]

w1w2 = w1*w2
v1dotv2 = dot_product(v1,v2)
w1v2 = scale_vector(v2,w1)
w2v1 = scale_vector(v1,w2)
v1crossv2 = cross_product(v1,v2)
w3 = w1w2-v1dotv2
v3 = add_vector(add_vector(w1v2,w2v1),v1crossv2)
q3 = [w3,v3[0],v3[1],v3[2]]
print(q3)