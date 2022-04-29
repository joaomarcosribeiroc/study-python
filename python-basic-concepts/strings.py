name = 'Brad'
age = 43

#Concatenate
#print('Hey, this is ' + name + ', he is ' + age) error
print('Hey, this is ' + name + ', he is ' + str(age)) 

#Formatting
#Positional Arguments

print('Name is  {name} and age is {age}'.format(name=name, age=age))

#F-Strings
print('Hello, my name is {name} and age is {age}') #Not work without
print(f'Hello, my name is {name} and age is {age}')

s = 'hello world'
print(s.capitalize)
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.count('l'))
print(s.startswith('hello'))
print(s.startswith('hello0'))
print(s.endswith('d'))
print(s.endswith('world'))
print(s.split())
print(s.isalpha())
print('print(s.replace(\' \', \'\').isalpha()): ')
print(s.replace(' ', '').isalpha())
print(s.isalnum())