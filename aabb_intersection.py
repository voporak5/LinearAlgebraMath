aabb1Min = [-7.5,-1,0.5]
aabb1Max = [-6.5,1,5.5]

aabb2Min = [-1.5,-1,3.5]
aabb2Max = [1.5,1,8.5]

def interval_overlap(min1,min2,max1,max2):
    max1min2 = max1 < min2
    max2min1 = max2 < min1

    if(max1min2 == False and max2min1 == False): return True
    else: return False


def intersect_aabb_aabb(min1,min2,max1,max2):
    x = interval_overlap(min1[0],min2[0],max1[0],max2[0])
    y = interval_overlap(min1[1],min2[1],max1[1],max2[1])
    z = interval_overlap(min1[2],min2[2],max1[2],max2[2])

    if(x == True and y == True and z == True): return True
    else: return False

print(intersect_aabb_aabb(aabb1Min,aabb2Min,aabb1Max,aabb2Max))