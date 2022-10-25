def factorial(n):
    if(n < 0):
        return -1
    if(n == 0):
        return 1
    x = 1
    for i in range(1 , n+1):
        x = x*i
    return x

def factorial_recursive(n):
    if(n < 0):
        return -1
    if(n == 0):
        return 1
    return n * factorial_recursive(n-1)

x = input("Input a whole number : ")
try:
    x = int(x)
except ValueError:
    print("Not an integer")
    exit()
print("Factorial of "+str(x) + " is equal to : "+str(factorial(x)))
print("Factorial of "+str(x) + " calculated using recursion is equal to : "+str(factorial_recursive(x)))