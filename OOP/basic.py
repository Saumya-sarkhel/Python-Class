class Test:
    x=None
    y=None

    def get(self):
        self.x=int(input("Enter the value of x: "))
        self.y=int(input("Enter the value of y: "))

    def display(self):
        print("x :",self.x)
        print("y :",self.y)

ob1=Test()
ob1.get()
ob1.display()
