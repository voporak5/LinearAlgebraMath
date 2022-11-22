import math

u = 0.1
p = [0.55557,0.35454,-0.5318,0.53181]
q = [0.55557,0.53181,-0.3545,-0.5318]

def dot_product(u,v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    z = u[2] * v[2]
    w = u[3] * v[3]
    dot = x + y + z + w;
    return dot

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    w = v[3] * s
    return [x,y,z,w]

def add_vector(v,v2):
    x = v[0] + v2[0]
    y = v[1] + v2[1]
    z = v[2] + v2[2]
    w = v[3] + v2[3]
    return [x,y,z,w]

cosTheta = dot_product(p,q)
#print(cosTheta)
theta = math.acos(cosTheta)
#print(theta)

fu = math.sin((1-u)*theta)/math.sin(theta)
#print(fu)

gu = math.sin(u*theta)/math.sin(theta)
#print(gu)

slerp = add_vector(scale_vector(p,fu),scale_vector(q,gu))
print(slerp)