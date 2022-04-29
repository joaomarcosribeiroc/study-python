#List is a collection that is ordered and changeble. Allow duplicate members.

#Create list

numbers = [1,2,3,4,5,6]
fruits = ['orange', 'apple', 'mango']

#Use a constructor
numbers2 = list((1,2,3,5))  

print('print(numbers[0])')
print(numbers[0])
print(fruits)
print("fruits.append('banana')")
fruits.append('banana')
print(fruits)
print("fruits.insert(1, 'strawberries')")
fruits.insert(1, 'strawberries')
print(fruits)
print("fruits.pop(1)")
fruits.pop(1)
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits[0] = 'blueberries'
print(fruits)
