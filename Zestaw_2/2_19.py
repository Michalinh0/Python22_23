list_of_numbers = [1 , 124 , 345 , 26 , 30 , 4 , 245]

list_of_strings = [str(item).zfill(3) for item in list_of_numbers]

string = ' '.join(list_of_strings)

print (string)