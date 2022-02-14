# A collection which is unordered, changeble, and indexed. No duplicate members.

# Create a dictionary

person = {
    'first_name':  'John',
    'last_nam': 'Doe',
    'age': 30
}

print(person, type(person))

person = dict(
    first_name='John',
    last_nam='Doe',
    age=30
)
print(person, type(person))


# Get Value
print("\nprint(person['first_name'])")
print(person['first_name'])
print("\nprint(person.get('first_name'))")
print(person.get('first_name'))

# Add value

person['phone'] = '555-555-555'
print("\nprint(person)")
print(person)

# Get dict Keys

print("\nprint(person.keys())")
print(person.keys())

# Get dict Keys itens

print("\nprint(person.items())")
print(person.items())

# Copy dict 
person2 = person.copy()
person2['city'] = 'Boston'
print("\n", person2)

# Remove Item

del(person['age'])
person.pop('phone')
print(person)

print("\nperson.clear()")
person.clear()
print(person)

person = dict(
    first_name='John',
    last_nam='Doe',
    age=30
)

print("\nprint(len(person))")
print(len(person))

# List of dict
persons = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Lucas', 'age': 30},
    {'name': 'Joseph', 'age': 30},
]
print("\nprint(len(persons))")
print(len(persons))

print("\nprint(persons)")
print(persons)

print("\nprint(persons[1]['name'])")
print(persons[1]['name'])

