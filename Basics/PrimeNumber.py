# Prime Number

n=int(input("Enter the number: "))
f=0
for i in range(1,(n+1),1):
  if(n%i == 0):
    f=f+1

if(f==2):
  print(n, " is prime")
elif(n==1):
  print(n, " is neither prime nor composite")
else:
  print(n, " is composite")
