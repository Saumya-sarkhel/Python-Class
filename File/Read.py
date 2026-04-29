fp=open("Read.txt","r")
print(fp.read())    # Read the existing file and prints it

print("File name:",fp.name)     # Print the file name
print("File mode:",fp.mode)     # Print the mode
print("File status:",fp.closed) # Print the status (close or not)
fp.close()
print("File status:",fp.closed)
