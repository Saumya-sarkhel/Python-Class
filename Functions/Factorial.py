# factorial using function

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Enter the number(by function): "))
print("The factorial is:",factorial(n))


# Factorial using function

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter the number(by recursion): "))
print("The factorial is:",fact(n))
