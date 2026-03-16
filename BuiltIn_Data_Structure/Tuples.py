"""
Tuples in Python are immutable, ordered collections of elements,
that can hold items of different data types.
Once created, their contents cannot be changed, making them ideal for storing fixed data.

Tuples are immutable and hashable.
Tuples can hold elements of different data types.
Tuples are more memory-efficient and faster than lists for read-only data.

"""
tup = ()        # Empty tuple
tup = (1,)      # Single value tuple
tup = (2, 5, 7, 11) # Integer tuple
print(type(tup))

tup = (5, 'Welcome', 7, 'Geeks') # Mixed
print(tup)

# Creating a Tuple with repetition
tup1 = ('Hello',) * 3
print(tup1)

# Accessing Tuple with Indexing
tup = tuple("Hello")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])
print(tup[:3])

# Concatenation of Tuples
tup1 = (1, 2, 3)
tup2 = ('Welcome', 'to', 'Class')

tup3 = tup1 + tup2
print(tup3)
