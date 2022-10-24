list = [[],[4],(1,2),[3,4],(5,6,7)]

sums = []

for i in list:
    sums.append(sum(i))


assert(sums == [0 , 4 , 3 , 7 , 18])
print(sums)