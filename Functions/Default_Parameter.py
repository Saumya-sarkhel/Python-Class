# Function
# Default parameter

def display(city="Mumbai"):
  print(city)


display("kolkata")
display()
display("Delhi")



def calc(a=0, b=0):  # here a, b gets the defaule value of 0 if no argument is passed
  c = a + b
  return c

print(calc(4, 5))
print(calc(4))
print(calc())
