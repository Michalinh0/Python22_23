def fibonacci(n):
    if(n <= 0):
        return -1
    if(n==1):
        return 0
    if(n==2):
        return 1
    x1 = 0
    x2 = 1
    for i in range(3 , n+1):
        temp = x1 + x2
        x1 = x2
        x2 = temp
    return x2

def fibonacci_recursive(n):
    if(n <= 0):
        return -1
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

x = input("Input a whole number : ")
try:
    x = int(x)
except ValueError:
    print("Not an integer")
    exit()
print("Element number "+str(x)+" in Fibonacci sequence is equal to : "+str(fibonacci(x)))
print("Element number "+str(x)+" in Fibonacci sequence calculated with recursion is equal to : "+str(fibonacci_recursive(x)))