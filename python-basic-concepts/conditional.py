x = 10 
y = 5

print("print(x > y)")
print(x > y)
print("print(x < y)")
print(x < y)
print("print(x != y)")
print(x != y)
print("print(x == y)")
print(x == y)
print("print(x >= y)")
print(x >= y)
print("print(x <= y)")
print(x <= y)

# If
print("\nif x > y:")
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is NOT greater than {y}')

print("\nIF ELIF ELSE")
if x < y:
    print(f'IF: {x} is smaller than {y}')
elif x == y:
    print(f'ELIF: {x} is equal to {y}')
else:
    print(f'ELSE: {x} is greater than {y}')
    
# Nested If
print("\nif x > y:")
if x > y:
    if x == 10:
        print(f'{x} is greater than {y} AND is 10')

# Nested If
print("\nif x > y and x == 10:")
if x > y and x == 10:
    print(f'{x} is greater than {y} AND is 10')

print("\nUsing in")
numbers = [1,2,3,4,5,6,7,8,9]
z = 10
if 10 == z:
    print(f'10 is equal to {z}')
