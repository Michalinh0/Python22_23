while(True):
    x = input("Podaj liczbe : ")
    try:
        if x.lower() == "stop":
            break
        x = float(x)
        print(x)
        print(str(x) + " " + str(x**3))
    except ValueError:
        print("Not a float")

