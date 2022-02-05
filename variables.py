"""
Variables Rules:
    - Variables names are case sensitive.
    - Variables names must start with a letter or underscore.
    - Variables names can have numbers but cannot start with a number.
"""

_yearsOld = 1 # int
weight = 58.6 # float
code = 'AD5DK569DOPMM000' #str
active = True #bool

#Multiple assignment
x, y, name, is_cool = (1, 2.5,'Jonh', False)

print('Hello')
print(x)
print(y, name)
print(x +y)
print(type(name))

x = str(x)//type transformation

print(type(x))