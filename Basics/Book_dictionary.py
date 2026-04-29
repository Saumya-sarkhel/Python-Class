n=int(input("Enter the no of Books: "))
print("\nID----Name----Author----Price")
m=int(input("Enter the no of fields for each Book: "))
vault=[]
for i in range(1, n+1):
    vault.append("Book-" +str(i))

print("Enter the fields of the books: ")
k=[]
for i in range(m):
    k.append(input("Enter the field: "))
val=[]
for i in range(1, n+1):
    print("\nEnter the records for Boook", i)
    v=[]
    for x in k:
        if (x.upper() == "ID"):
            v.append(int(input("Enter the ID: ")))
        if (x.upper() == "NAME"):
            v.append(input("Enter the Book Name: "))
        if (x.upper() == "AUTHOR"):
            v.append(input("Enter the Author: "))
        if (x.upper() == "PRICE"):
            v.append(float(input("Enter the Priec: ")))
    collect = dict(zip(k,v))
    val.append(collect)
book=dict(zip(collect, val))

print()
print("ID\tName\t\tAuthor\t\tPrice")
print("---------------------------------------------------------------------")
for e in book.values():
    for val in e.values():
        print(val, end="\t")
    print()

key=input("\nEnter the book name to find: ")
found = False
for e in book.values():
    if e["Name"].upper() == key.upper():
        print("Author Name:", e["Author"])
        found = True
        break

if found == False:
    print("Book not found")
