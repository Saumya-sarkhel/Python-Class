# 2D array using list

r1=int(input("enter the Row for 1st Matrix: "))
c1=int(input("enter the Col for 1st Matrix: "))
r2=int(input("enter the Row for 2nd Matrix: "))
c2=int(input("enter the Col for 2nd Matrix: "))
a=[]
b=[]
if(r1==r2 and c1==c2):
    print("Enter the 1st Matrix data: ")
    for i in range(r1):
        t=[]
        for j in range(c1):
            t.append(int(input()))
        a.append(t)

    print("Enter the 2nd Matrix data: ")
    for i in range(r2):
        t=[]
        for j in range(c2):
            t.append(int(input()))
        b.append(t)

    print("1st matrix: ")
    for x in a:
        for y in x:
            print(y,end=" ")
        print()

    print("2nd matrix: ")
    for x in b:
        for y in x:
            print(y,end=" ")
        print()
    c=[]
    for i in range(r1):
        t=[]
        for j in range(c1):
            t.append(a[i][j]+b[i][j])
        c.append(t)

    print("\nAddition Matrix Is: ")
    for i in range(r1):
        for j in range(c1):
            print(c[i][j],end=" ")
        print()

else: print("Addition not posible")
