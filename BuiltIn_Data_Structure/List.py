"""
Python Lists are a fundamental data structure used to store an ordered,
mutable collection of items.
They are defined using square brackets [] and can hold elements of different data types,
such as integers, strings, booleans, or even other lists.

Key Features:
Ordered: Elements maintain their position; access via index (starting at 0).
Mutable: Items can be added, removed, or modified after creation.
Heterogeneous: Can contain mixed data types.
Allow duplicates: Same value can appear multiple times.

"""

# Using Square Brackets
a = [1, 2, 3, 4, 5, 2]                # Integers
b = ['apple', 'banana', 'cherry']  # String
c = [1, 'hello', 3.14, True]       # Mixed Data types

print(a)
print(b)
print(c)
print() # Print blank line



# Using list() Constructor
a = list((1, 2, 3, 'apple', 4.5))
print(a)

b = list("Hello Python")
print(b)

# List Slicing -> list_name[starting_index : ending_index] ending_index in excluded
print(b[2:8])
print()



# Operations in Lists
a = []
print("Initial list:", a)

a.append(10)
print("After append(10):", a)

a.insert(0, 5)
print("After insert(0, 5):", a)

a.extend([7, 3, 12, 9])
print("After extend([7, 3, 12, 9]):", a)

a.reverse()
print("Afte reverse the list:", a)

a.sort()
print("After sorting (Ascending Order):", a)

a.sort(reverse=True)
print("After sorting(Descending Order):", a)

a.clear()
print("After clear():", a)
print()


# Methods
list = [1, 4, 2, 7]
list.remove(4) # remove first occurence of element
print(list)

list = [1, 4, 2, 7]
list.pop(2) # 2nd index value pop
print(list)
