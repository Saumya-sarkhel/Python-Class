# Pattern print 4

row = int(input("Enter the number of rows: "))
k=1
for i in range(1, row + 1):
    for j in range(1, (i+1)):
      print(k, end=" ")
      k+=1
    print()


"""
Sample:

1
2 3
4 5 6
7 8 9 10

"""
