# Create a function

def say_hello(name):
    print(f'Hello {name}')

print("\nsay_hello('João Marcos')")
say_hello('João Marcos')


def getSum(num1, num2):
    total = num1 + num2
    return total

print("\nprint('\\n', getSum(5,8))")
print('\n', getSum(5,8))

print("\nprint(getSum(8,5))")
getSum = lambda num1, num2 : num1 + num2
print(getSum(8,5))
