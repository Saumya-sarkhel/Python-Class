# Maximum of 3 Number

x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
z=int(input("Enter the 3rd number:"))

if(x==y and x==z):
    print("ALL are equal")
elif(x>y and x>z):
    print(x,"is maximum")
elif(y>x and y>z):
    print(y,"is maximum")
else:
    print(z,"is maximum")
