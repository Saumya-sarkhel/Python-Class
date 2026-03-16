# Pattern print 5

row = int(input("Enter the number of rows: "))
for i in range(1, row + 1):
    for j in range(1, (i+1)):
      print(j%2, end=" ")
    print()


"""
Sample:

1
1 0
1 0 1
1 0 1 0

"""
