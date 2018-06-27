#Regex
import re


# By putting the r before the first quote of string value,
# can mark string to raw string
phoneNumRegex = re.compile(r'(\d\d\d\d)(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 91225555')
# Only show group one
print('Phone number found: ' + mo.group(1))
print('Whole thing: ' + str(mo.groups()))

# * 0->n || + 1->n

# {8} mean repeat the condition for n times
# PhoneNumber Filter can be rewritten into
phoneNumRegex = re.compile(r'\d{8}')
mo = phoneNumRegex.search('My number is 12345678')
print('Phone number found: ' + str(mo) )
input()