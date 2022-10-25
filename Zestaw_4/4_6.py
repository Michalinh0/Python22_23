def sum_seq(seq):
    sum = 0
    for item in seq:
        if(isinstance(item,(list , tuple))):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print("Suma liczb w sekwencji to : " + str(sum_seq(seq)))