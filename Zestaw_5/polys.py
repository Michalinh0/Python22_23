import unittest

def add_poly(p1 , p2):
    result = []
    for i in range(max(len(p1) , len(p2))):
        if(i == len(p1)):
            p1.append(0)
        if(i == len(p2)):
            p2.append(0)
        result.append(p1[i] + p2[i])
    return result

def sub_poly(p1 , p2):
    result = []
    for i in range(max(len(p1) , len(p2))):
        if(i == len(p1)):
            p1.append(0)
        if(i == len(p2)):
            p2.append(0)
        result.append(p1[i] - p2[i])
    return result



p1 = [0 , 1]
p2 = [0 , 1 , 2]

print(add_poly(p1 , p2))
print(add_poly(p1 , p2))