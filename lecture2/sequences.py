name = "Harry"

print(name[0]) # print the 0th element of name
print(name[1])

# list, sequence of mutable values
names = ["Harry", "Ron", "Hermione", "Ginny"]
print(names)
print(names[0])

names.append("Draco")
names.sort()
print(names)

# tuple, sequence of immutable values
coordinate = (10.0, 20.0)

# set, collection of unique values (in any order)
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # won't re-add 3
print(s)

s.remove(2)
print(s)
print(f"The set has {len(s)} elements.") # len works on all sequence data types

# dict, collection of key-value pairs
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])

houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])