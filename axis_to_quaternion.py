import math

#give the quaternion that represents a rotation
#by theta radian around the axis r

theta = -1*math.pi/8
r = [3,0,-1]


def vec_normalize(v):
    xSquare = v[0] * v[0]
    ySquare = v[1] * v[1]
    zSquare = v[2] * v[2]
    magnitude = math.sqrt(xSquare + ySquare + zSquare)
    vNorm = [v[0]/magnitude,v[1]/magnitude,v[2]/magnitude]
    return vNorm

def scale_vector(v,s):
    x = v[0] * s
    y = v[1] * s
    z = v[2] * s
    return [x,y,z]

rNorm = vec_normalize(r)

w = math.cos(theta/2)
v = scale_vector(rNorm,math.sin(theta/2))

q = [w,v[0],v[1],v[2]]

print(q)