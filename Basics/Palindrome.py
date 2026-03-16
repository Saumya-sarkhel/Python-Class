# Palindrome uisng list

list1 = [1, 2, 1]
list2 = ['m', 'a', 'd', 'a', 'm']

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list1 == list1):
    print("This is palindrome")
else:
    print("This is not Palindrome")


if(copy_list2 == list2):
    print("This is palindrome")
else:
    print("This is not Palindrome")
