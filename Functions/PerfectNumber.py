"""
Example:
6 is perfect because its divisors (1, 2, 3) sum to 6 (1 + 2 + 3 = 6).
The next perfect number is 28 (1 + 2 + 4 + 7 + 14 = 28).

"""

def perfect_number(num):
    f = 0
    for i in range(1, num):
        if num % i == 0:
            f += i
    if (f == num):
        print("This is a perfect number.")
    else:
        print("This is not perfect number.")


num = int(input("Enter the number: "))
perfect_number(num)
