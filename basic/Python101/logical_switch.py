# Following block of code how basic logical statement like if, while, for else.
# To work on python

# If
# The scope would least till hit else:
myName = input("Your name plz?")
if myName == 'Andy':
    print('Hello Andy')
else:
    print('Hello, Stranger')


# If...else...if
if myName == 'Andy':
    print('Hello Andy again.')
elif myName == 'Ken':
    print('Ha ken, Andy is not comin?')


# For loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# For in range of number: 12 to 16
for i in range(12, 16):
    print(i)

# 0 to 10 increment 2 per step
for i in range(0, 10, 2):
    print(i)




# While loop
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam +1

# While not, which come especially useful for filtering?
# Of course
name = ''
while not name:  # (1)
    print('Enter your name:')
    name = input( )

