# Pattern print 8
# Alternate verse of pattern 2

row = int(input("Enter the number of rows: "))
for i in reversed(range(1, row+1)):
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
