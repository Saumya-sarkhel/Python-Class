class Complex:
    real=None
    img=None

    def get(self):
        self.real=int(input("Enter the real no: "))
        self.img=int(input("Enter the imaginary no: "))

    def display(self):
        # print("Real :",self.real)
        # print("Imaginary :",self.img)
        print((self.real),"+ i",(self.img))

    def add(self, ob1, ob2):
        self.real = ob1.real + ob2.real
        self.img = ob1.img + ob2.img


c1=Complex()
c2=Complex()

print("Input first complex no: ")
c1.get()
print("Input second complex no: ")
c2.get()
print()

print("First complex no is: ")
c1.display()
print("Second complex no is: ")
c2.display()
print()

c3=Complex()
c3.add(c1, c2)
print("Afte addition: ")
c3.display()
