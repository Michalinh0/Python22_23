x = input("Podaj dlugosc : ")
try:
    x = int(x)
except ValueError:
    print("Not an integer")
    exit()
res = "|" + "....|"*x
res = res + "\n0"
for i in range(1 , x+1):
    res = res + str(i).rjust(5)
print(res)