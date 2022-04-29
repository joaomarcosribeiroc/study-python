myFile  = open('my-file.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

myFile.write('Learning file\n')
myFile.write('Finished')
myFile.close()

myFile  = open('my-file.txt', 'a')
myFile.write('Web development')
myFile.close()

myFile  = open('my-file.txt', 'r+')
print(myFile.read(10))

