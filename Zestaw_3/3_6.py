length = input("Podaj dlugosc : ")
height = input("Podaj wysokosc : ")

try:
    length = int(length)
    height = int(height)
except ValueError:
    print("Not an integer")
    exit()

result = ""
for i in range(height):
    result += "+" + "---+"*length
    result += '\n'
    result += "|   "*length + '|'
    result += '\n'
result += "+" + "---+"*length
result += '\n'

print(result)





