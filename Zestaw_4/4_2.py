def make_ruler(n):
    res = "|" + "....|"*n
    res = res + "\n0"
    for i in range(1 , n+1):
        res = res + str(i).rjust(5)
    return res

def make_grid(rows , cols):
    result = ""
    for i in range(rows):
        result += "+" + "---+"*cols
        result += '\n'
        result += "|   "*cols + '|'
        result += '\n'
    result += "+" + "---+"*cols
    result += '\n'
    return result

n = input("Input length : ")
try:
    n = int(n)
except ValueError:
    print("Not an integer")
    exit()
print(make_ruler(n))

cols = input("Input length : ")
rows = input("Input height : ")

try:
    cols = int(cols)
    rows = int(rows)
except ValueError:
    print("Not an integer")
    exit()
print(make_grid(rows , cols))