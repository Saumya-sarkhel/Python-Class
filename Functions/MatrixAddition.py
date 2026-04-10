def input_Matrix(k):
    for i in range(r1):
        t=[]
        for j in range(c1):
            t.append(int(input()))
        k.append(t)
    return k

def display_Matrix(k):
    for i in range(r1):
        for j in range(c1):
            print(k[i][j],end=" ")
        print()

r1=int(input("enter the Row for 1st Matrix: "))
c1=int(input("enter the Col for 1st Matrix: "))
r2=int(input("enter the Row for 2nd Matrix: "))
c2=int(input("enter the Col for 2nd Matrix: "))
a=[]
b=[]
if(r1==r2 and c1==c2):
    print("Enter the 1st Matrix data:")
    input_Matrix(a)
    print("Enter the 2nd Matrix data:")
    input_Matrix(b)
    print("1st matrix:")
    display_Matrix(a)
    print("2nd matrix:")
    display_Matrix(b)

    #addition
    c=[]
    for i in range(r1):
        t=[]
        for j in range(c1):
            t.append(a[i][j] + b[i][j])
        c.append(t)
    print("\nAddition Matrix Is: ")
    display_Matrix(c)

else:
    print("Addition not posible")
