class Test:
    x = None

    def __init__(self): # Default Constructor
        print("Constructor called..")

    # Deleting (Calling destructor)
    def __del__(self):
        print("Destructor called..")

    def get(self):
        self.x = int(input("Enter the number: "))

    def display(self):
        print("Number is:",self.x)


ob1 = Test()
ob2 = Test()
del ob1
