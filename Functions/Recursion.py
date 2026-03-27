# recursive function
# print n to 1 backwards

def show(n):
    if (n == 0):  # Stopping condition / base case
        return
    print(n)
    show(n-1)   # recursive call

show(5)
