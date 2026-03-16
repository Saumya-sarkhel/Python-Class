# Nested if-else (Maximum of 3 number)

x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
z=int(input("Enter the 3rd number:"))

if(x==y and x==z):
    print("ALL are equal")
else:
    if(x>y):
        if(x>z):
            max=x
        else:
            max=z
    else:
        if(y>z):
            max=y
        else:
            max=z
print("Maximum is:",max)
