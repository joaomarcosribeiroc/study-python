# A tuple is a collection that is ordered and unchangeble. Allow duplicate members.
 # Create a tuple.

fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

fruits3 = ('Apples')
fruits4 = ('Apples',)
print(fruits3, type(fruits3)) # String type
print(fruits4, type(fruits4))
print("\nprint(fruits4[0])")
print(fruits4[0])

print("\nfruits4[0] = 'add' # give error")
#fruits4[0] = 'add' # give error

del fruits
# print(fruits) # give error

print("\nprint(len(fruits3))")
print(len(fruits3))