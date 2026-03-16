# Pattern print 12

row = int(input("Enter the number of rows: "))
for i in reversed(range(1, row+1)):

  for j in range(1, (row-i)+1):
    print(" ", end=" ")

  for j in range(1, (i+1)):
    print("*", end=" ")
  print()


"""
Sample:

* * * *
  * * *
    * *
      *

"""
