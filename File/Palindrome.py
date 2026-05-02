# Check words are palindrome or not in a file

fp=open("palindrome.txt","r")
msg=fp.read()
w=msg.split("\n")
fp.seek(0,0)
print("palindromes are: ")
for i in range(len(w)):
    s=fp.readline()
    s=s.strip()  # removes specified characters from both the beginning and the end of a string.(space, tab ..)
    a=s.split(" ")
    for s in a:
        if(s==s[::-1]):
            print(s)
fp.close()
