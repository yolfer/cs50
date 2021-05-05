people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

# people.sort() won't work! py doesn't know how to sort dicts

def f(person):
    return person["name"]

# people.sort(key=f)

# represent function inline with a lambda
# 'person' is input, 'person[name]' is output
people.sort(key=lambda person: person["name"])

print(people)