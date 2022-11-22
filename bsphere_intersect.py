import math

c1 = [9.856,0,4.102]
r1 = 1.5

c2 = [10,0,-7]
r2 = 2.5

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

def collide_sphere(c1,c2,r1,r2):
    c1Minusc2 = sub_vector(c1,c2)
    magnitude = vec_magnitude(c1Minusc2)
    r1Plusr2 = r1 + r2
    if(magnitude < r1Plusr2): return True
    else: return False

print(collide_sphere(c1,c2,r1,r2))