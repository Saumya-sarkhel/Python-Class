# Pattern print 7

row = int(input("Enter the number of rows: "))
k=0
for i in range(1, row + 1):
    for j in range(1, (i+1)):
      print(k%2, end=" ")
      k+=1
    print()


"""
Sample:

0
1 0
1 0 1
0 1 0 1

"""
