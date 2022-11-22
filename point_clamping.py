p = [2,0,-9]
min = [-8.5,-1,-7]
max = [-5.5,1,-5]

def clamp_point(p,min,max):

    pPrime = [0,0,0]

    if(p[0] < min[0]): pPrime[0] = min[0]
    elif(p[0] > max[0]): pPrime[0] = max[0]
    else: pPrime[0] = p[0]

    if(p[1] < min[1]): pPrime[1] = min[1]
    elif(p[1] > max[1]): pPrime[1] = max[1]
    else: pPrime[1] = p[1]

    if(p[2] < min[2]): pPrime[2] = min[2]
    elif(p[2] > max[2]): pPrime[2] = max[2]
    else: pPrime[2] = p[2]

    return pPrime

print(clamp_point(p,min,max))