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

r1=int(input("Enter the Row for Matrix: "))
c1=int(input("Enter the Col for Matrix: "))

a=[]

print("Enter the Matrix data:")
input_Matrix(a)

print("Original Matrix:")
display_Matrix(a)

# transpose
c=[]
for i in range(c1):
    t=[]
    for j in range(r1):
        t.append(a[j][i])
    c.append(t)

print("\nTranspose Matrix Is: ")

r1, c1 = c1, r1
display_Matrix(c)
