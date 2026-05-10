class Student:
    roll = None
    name = None
    marks = None

    def inputRecord(self):
        self.roll = int(input("Enter the roll: "))
        self.name = input("Enter the name: ")
        self.marks = float(input("Enter the marks: "))

    def DisplayRecord(self):
        print(self.roll,"\t",self.name,"\t",self.marks)


n=int(input("No of students: "))
stu=[]
for i in range(n):
    s=Student()
    print("Enter the record for Student",(i+1))
    s.inputRecord()
    stu.append(s)

print("Records of the Students: ")
print("\nRoll\t","Name\t","Marks")
for s in stu:
    s.DisplayRecord()
