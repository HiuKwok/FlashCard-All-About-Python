import random

# Prompt user for input
print('Hello world!')
myName = input( )

# Type convert
print(len(myName))
print('What is your age? ')
myAge = input( )
print('You will be ' + str(int(myAge) + 1) + ' in a year. ')

# Random module
for i in range(5):
    print(random.randint(1, 10))


#Method call
def hello (name):
	print("Hello " + name)
	if name == "Andy":
		return True


owner = hello("Andy")
#None == null
print("Owner: " + str(None != owner) )


#Try && except
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')



