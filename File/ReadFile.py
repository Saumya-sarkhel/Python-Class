# Read an unknown file content

fp=open("readFile.txt","r")
msg=fp.read()
w=msg.split("\n")
# print(w)
print("No of lines:",len(w))

# seek(offset, whence)
# whence is file pointer location
# [0 = Begining], [1 = current], [2 = end]
fp.seek(0,0)
for i in range(len(w)):
    print("Line",(i+1),"is:",fp.readline(),end="")
