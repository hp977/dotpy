# nesting of data structure 

people = [
    {"name": "Harry", "house": "Gryfinder"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slythorin"}
]
def f(person):
    return person["name"]

people.sort(key=f)
# people.sort(key=lamda person:person["name"])
print(people)
