def make_ruler(n):
    upper = []
    lower = ['0']
    upper.append("....".join('|'*(n+1)))
    for i in range(1 , n+1):
        lower.append(str(i).rjust(5))
    return ''.join(upper) + '\n' + ''.join(lower)

def make_grid(rows , cols):
    lines = []
    for i in range(2*rows + 1):
        if(i % 2 == 0):
            lines.append("---".join('+'*cols))
        else:
            lines.append("   ".join('|'*cols))
    return '\n'.join(lines)

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