def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)

print("Factorial is: ", fact(3))
print("Fib is: ", fib(3))
