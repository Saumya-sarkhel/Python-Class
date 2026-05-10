class Test:
    x = None

    def display(self):
        print("Display is called")

    def __str__(self):
        return "Display is called new way"

ob1 = Test()
print(ob1)


"""
The __str__ method is called when the following functions are invoked on the object
and return a string:

  (i)   The print() method
  (ii)  The str() method

"""
