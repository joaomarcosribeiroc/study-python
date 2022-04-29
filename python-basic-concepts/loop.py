people = ['John', 'Sarah', 'Paul']

for person in people:
    print(person)

print("\n1:")

for person in people:
    if person == 'John':
        continue
    print(person)

print("\n2:")

for person in people:
    if person == 'Sarah':
        break
    print(person)

print("\n3:")

for person in people:
    if person == 'Sarah':
        break
    print(person)

print("\n4:")

for i in range(len(people)):
    print(people[i])

print("\n5:")

for i in range(1,5):
    print(i)

print("\n6:")
count = 0
while(count < 10):
    print(count)
    count += 1