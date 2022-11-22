import math

obb1W = [[1.591,1.083,0.544,5],
         [0.477,-1.39,1.361,0],
         [1.114,-0.95,-1.36,8],
         [0,0,0,1]]

obb2W = [[0.544,-1.92,0,7],
         [1.361,0.385,1.414,0],
         [-1.36,-0.38,1.414,-6],
         [0,0,0,1]]

s1Enabled = 1
u1Enabled = 0
f1Enabled = 0

s2Enabled = 0
u2Enabled = 0
f2Enabled = 1

s1Xs2Enabled = 0
s1Xu2Enabled = 0
s1Xf2Enabled = 1

u1Xs2Enabled = 0
u1Xu2Enabled = 0
u1Xf2Enabled = 0

f1Xs2Enabled = 0
f1Xu2Enabled = 0
f1Xf2Enabled = 0

def cross_product(u,v):
    x1 = u[1] * v[2]
    x2 = v[1] * u[2]
    y1 = u[2] * v[0]
    y2 = v[2] * u[0]
    z1 = u[0] * v[1]
    z2 = v[0] * u[1]

    cross = [x1 - x2,y1 - y2,z1 - z2]
    return cross

s1 = [obb1W[0][0],obb1W[1][0],obb1W[2][0]]
u1 = [obb1W[0][1],obb1W[1][1],obb1W[2][1]]
f1 = [obb1W[0][2],obb1W[1][2],obb1W[2][2]]

s2 = [obb2W[0][0],obb2W[1][0],obb2W[2][0]]
u2 = [obb2W[0][1],obb2W[1][1],obb2W[2][1]]
f2 = [obb2W[0][2],obb2W[1][2],obb2W[2][2]]

if(s1Enabled == True): print(s1)
if(u1Enabled == True): print(u1)
if(f1Enabled == True): print(f1)

if(s2Enabled == True): print(s2)
if(u2Enabled == True): print(u2)
if(f2Enabled == True): print(f2)

if(s1Xs2Enabled == True): print(cross_product(s1,s2))
if(s1Xu2Enabled == True): print(cross_product(s1,u2))
if(s1Xf2Enabled == True): print(cross_product(s1,f2))

if(u1Xs2Enabled == True): print(cross_product(u1,s2))
if(u1Xu2Enabled == True): print(cross_product(u1,u2))
if(u1Xf2Enabled == True): print(cross_product(u1,f2))

if(f1Xs2Enabled == True): print(cross_product(f1,s2))
if(f1Xu2Enabled == True): print(cross_product(f1,u2))
if(f1Xf2Enabled == True): print(cross_product(f1,f2))