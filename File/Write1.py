# Write content with user input
fp=open("write1.txt","w") # In write mode existing file overrides with new content
choice='y'
while(choice =='y'):
    msg=input("Enter the msg: ")
    fp.write(msg+"\n")
    choice=input("Do you want to add more? y(yes)/n(no):")
fp.close()
