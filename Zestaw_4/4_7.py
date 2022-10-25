def flatten(seq):
    result = []
    for item in seq:
        if(isinstance(item,(list , tuple))):
            temp_list = flatten(item)
            for i in temp_list:
                result.append(i)
        else:
            result.append(item)
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))
        