def roman2int(number):
    result = conversion.get(number[0])
    previous = number[0]
    number = number[1:]
    for i in number:
        if(conversion.get(i) > conversion.get(previous)):
            result -= 2*conversion.get(previous)
        result += conversion.get(i)
        previous = i
        print(result)
    return result
    
#Sposób 1 - inicjacja z danymi

conversion = {'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}

#Sposób 2 - inicjacja z użyciem listy tuple

list = [('I' , 1) , ('V' , 5) , ('X' , 10 ) , ('L' , 50) , ('C' , 100) , ('D' , 500) , ('M' , 1000)]
conversion2 = dict(list)

#Sposób 3 - z użyciem dwóch list

keys = ['I' , 'V' , 'X' , 'L' , 'C' , 'D' , 'M']
values = [1 , 5 , 10 , 50 , 100 , 500 , 1000]
conversion3 = dict(zip(keys , values))

assert(conversion == conversion2 == conversion3)

print(roman2int('CMXCIX'))

