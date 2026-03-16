"""
Sets in Python are unordered collections of unique elements,
meaning they automatically eliminate duplicates and do not maintain a specific order.
They are mutable, allowing you to add or remove items, but do not support indexing or slicing.
sets -> mutable; sets -> elements -> immutable

key Features:

Unique Elements: Sets only store distinct values; any duplicates are automatically removed.
Unordered: Items have no fixed position, so their order may vary between executions.
Mutable: You can modify a set after creation using methods like add() and remove().
Hashable Elements Only: Sets can contain immutable types like numbers, strings, and tuples, but not lists or dictionaries.

"""

s = {10, 50, 20}
s1 = {10, 50, 10, "hello", "world"}   # Duplicate values are ignored

print(s)
print(s1)
print(type(s1))
print("Length is:", len(s1))

print("----")

"""
Methods:

set.add(): adds an element
set.remove(el): removes the element el
set.clear(): empties the set
set.pop(): removes a random value

"""

collection = set() # empty set

# add
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("apple")
collection.add("mango")

print(collection)

# remove
collection.remove(1)
print(collection)

# clear
collection.clear()
print(collection)


# pop
collection = {"apple", "mango", "banana", "cherry"}
print(collection.pop())

print("----")


# Union
set1 = {1, 2, 3}
set2 = {4, 2, 5, 1}

print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) #{1, 2}
