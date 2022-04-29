# Sets is a collection which is unordered and unidexed. No duplicate members

# Create a Set
fruits_set = {'Apples', 'Oranges', 'Grapes'}

# Check if in set 
print("\nprint('Apples' in fruits_set)")
print('Apples' in fruits_set)

# Add to Set
fruits_set.add('Grape')
print(fruits_set)

# Add from Set
print("\nfruits_set.remove('Grape')")
fruits_set.remove('Grape')
print(fruits_set)

# Add from Set
print("\nfruits_set.clear()")
fruits_set.clear()
print(fruits_set)

# Do not add twice
fruits_set = {'Apples', 'Oranges', 'Grapes'}
print("\nfruits_set.add('Apples')")
fruits_set.add('Apples')
print(fruits_set)
