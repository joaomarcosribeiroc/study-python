print("\n4:")

class User:
    # Constructor
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f'My name is {self.name}'
    def say(self):
        return f'Hi'

class Costumer(User):
    # Constructor
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self): # overriding
        return f'My name is {self.name}'

user = User('Brad')

print("\n2:")
print(user.name)
print("\n3:")
print(type(user))
print("\n5:")
print(user.greeting())

print("\n6:")

abe = Costumer('Abe')
abe.set_balance(52)
abe.greeting()

print(abe.greeting())
print(abe.say())