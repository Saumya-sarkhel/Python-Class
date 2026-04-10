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

r1=int(input("Enter the Row for 1st Matrix: "))
c1=int(input("Enter the Col for 1st Matrix: "))
r2=int(input("Enter the Row for 2nd Matrix: "))
c2=int(input("Enter the Col for 2nd Matrix: "))

a=[]
b=[]
if(c1==r2):
    print("Enter the 1st Matrix data:")
    input_Matrix(a)
    print("Enter the 2nd Matrix data:")
    input_Matrix(b)

    print("1st Matrix:")
    display_Matrix(a)
    print("2nd Matrix:")
    display_Matrix(b)

    # multiplication
    r3 = r1
    c3 = c2
    c = []
    for i in range(r3):
        t=[]
        for j in range(c3):
            sum_val = 0
            for k in range(c1):
                sum_val += a[i][k] * b[k][j]
            t.append(sum_val)
        c.append(t)

    print("\nMultiplication Matrix Is: ")
    r1, c1 = r3, c3
    display_Matrix(c)

else:
    print("Multiplication not possible")
