# Stack using list:

def push(stack,maxSize,top):
    if(top==maxSize-1):
        print("Stack is full")
    else:
        data=int(input("Enter the data:"))    
        top=top+1
        stack.append(data)
    return top

def pop(stack,top):
    if(top==-1):
        print("Stack is empty.")
    else:
        data=stack.pop()
        top=top-1
        print("Deleted data is:",data)    
    return top

def display(stack,top):
    if(top==-1):
        print("Stack is empty.")
    else:
        print("Stack elements are:")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])

def peek(stack,top):
    if(top==-1):
        print("Stack is Empty")
    else:
        print("Top most data of the stack is: ",stack[top])

maxSize=int(input("Enter the max size of the stack:"))
stack=[]
top=-1

while True:
    print("1.PUSH\n2.POP\n3.DISPLAY\n4.PEEK\n5.EXIT\n")
    choice=int(input("Enter your choice:"))

    if(choice==1):
        top=push(stack,maxSize,top)
    elif(choice==2):
        top=pop(stack,top)
    elif(choice==3):
        display(stack,top)
    elif(choice==4):
        peek(stack,top)
    elif(choice==5):
        break               
    else:
        print("Enter a valid choice...")