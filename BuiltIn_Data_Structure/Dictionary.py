"""
A Python dictionary is a data structure that stores information in [key-value] pairs.
While keys must be unique and immutable (like strings or numbers),
the values can be of any data type, whether mutable or immutable.

This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.

"""

data = {
    "name": "John",
    "age": 22
}
print(data)
print("-------")


info = {
    "name": "John",
    "age": 21,
    "Subject": ["python", "Java", "SQL"],       # List
    "topic": ("dict", "set", "list", "tuple"),  # Tuples
    "is_adult": True,
}
print(info)
print(info.get("name"))
print("The age is:",info["age"])
print("-------")

# Updating name in dictionary
info["name"] = "David"
print(info.get("name"))
print("-------")


# using dict() constructor
d2 = dict(a = "Welcome", b = "to", c = "Class")
print(d2)
print("-------")


# Nested Dictionary

student = {
    "name": "David John",
    "age": 22,
    "subject":{
        "phy": 96,
        "chem": 87,
        "math": 94
    }
}
print(student)
print(student["subject"])
print("-------")
