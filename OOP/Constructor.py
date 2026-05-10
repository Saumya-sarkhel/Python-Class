class Test:
    x = None

    def __init__(self): # Default Constructor
        print("Constructor called..")

    def get(self):
        self.x = int(input("Enter the number: "))

    def display(self):
        print("Number is:",self.x)


ob1 = Test()  # Object creates and calls Constructor
ob2 = Test()  # Object creates and calls Constructor
ob1.get()
ob1.display()
