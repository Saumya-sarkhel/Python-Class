def enqueue(q,maxSize,front,rear):
    if(rear==(maxSize-1)):
        print("Queue is full...\n")
    else:
        rear=rear+1
        data=int(input("Enter the data:"))	
		
        q.append(data)
        if(rear==0):
            front=0
    return front,rear

def dequeue(q,front,rear):
    if(rear==-1 and front==-1):
        print("Queue is empty...\n")
    else:
        data=q[front]
        if rear==front:
            rear=-1
            front=-1
        else:
            front=front+1
        print("Deleted element is:",data)    
    return front,rear

def display(q,front,rear):
    if(rear==-1 and front==-1):
        print("Queue is empty...\n")
    else:
        print("Queue elements are:")
        for i in range(front,rear+1):
            print(q[i],"|",end="")    


rear=-1
front=-1
q=[]
maxSize=int(input("Enter the max size of the queue:"))

while True:
    print("\n1.ENQUEUE\n2.DEQUEUE\n3.DISPLAY\n4.EXIT\n")
    choice=int(input("Enter your choice:"))

    if(choice==1):
        front,rear=enqueue(q,maxSize,front,rear)
    elif(choice==2):
        front,rear=dequeue(q,front,rear)
    elif(choice==3):
        display(q,front,rear)
    elif(choice==4):
        break
    else:
        print("Enter a valid choice...")

