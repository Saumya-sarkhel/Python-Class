n=int(input("Enter the no of employe: "))
print("\nFields: ID--NAME--SALARY")
m=int(input("Enter the no of fields for each employee: "))
emp=[]
for i in range(1, n+1):
    emp.append("Employee-" +str(i))

print("Enter the fields of employee: ")
k=[]
for i in range(m):
    k.append(input("Enter the field: "))
val=[]
for i in range(1, n+1):
    print()
    print("Enter the records for employe", i)
    v=[]
    for x in k:
        if (x.upper() == "ID"):
            v.append(int(input("Enter the ID: ")))
        if (x.upper() == "NAME"):
            v.append(input("Enter the Name: "))
        if (x.upper() == "SALARY"):
            v.append(float(input("Enter the Salary: ")))
    employ = dict(zip(k,v))
    val.append(employ)
emp=dict(zip(employ, val))

print()
print("ID\tName\t\tSalary")
print("------------------------------")
for e in emp.values():
    for val in e.values():
        print(val, end="\t")
    print()
