# Import a core python module

import datetime 
from datetime import date
import time

print("\n1:")
today = datetime.date.today()
print(today)

print("\n2:")
today2 = date.fromtimestamp(19293445)
print(today2)

print("\n3:")
time = time.time()
print(time)

print("\n4:")
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello my name is john'))

print("\n4:")
# import custom module
import validator
from validator import validate_email

for email in ['test@test.com', 'testtest.com']:
    if(validate_email(email)):
        print(f'{email} is a valid email')
    else:
        print(f'{email} is NOT a valid email')
