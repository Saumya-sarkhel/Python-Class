"""
Operations:

del: removes an item using its key
pop(): removes the item with the given key and returns its value
clear(): removes all items from the dictionary
popitem(): removes and returns the last inserted key-value pair

"""

dict = {
    1: 'Apple',
    2: 'Banana',
    3: 'Mango',
    "age": 22
}

# Using del
del dict["age"]
print(dict)

# Using pop()
val = dict.pop(1)
print(val)

# Using popitem()
key, val = dict.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
dict.clear()
print(dict)

print("-------")



"""
Methods:

dict.keys(): Returns all keys
dict.values(): returns all values
dict.items(): returns all key-value pairs as tuples
dict.get("key"): returns the key according to value
dict.update(new_dict): inserts the specified item to the dictionary

"""

student = {
    "name": "David John",
    "age": 22,
    "subject":{
        "phy": 96,
        "chem": 87,
        "math": 94
    }
}

# total no of keys in dictionary
print(len(student))

print(student.keys())
print(list(student.keys())) # List typecastng
print("-------")

print(student.values())
print(list(student.values()))
print("-------")

print(student.items())
print("-------")

print(student["name"])      # returns error if not match
print(student.get("name"))  # returns "None" if not match
print("-------")

student.update({"city": "Delhi"})
print(student)
