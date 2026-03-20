rows = int(input("Enter the row size: "))
for i in range(rows, 0, -1):

    for j in range(rows  - i):
        print(" ", end=" ")

    for k in range(1, 2*i):
        print("*", end=" ")

    print()



"""
Sample:

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""
