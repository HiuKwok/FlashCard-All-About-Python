import shutil, os
import os


# Mkdir
# os.makedirs('BasicModule')

# Get absolute path
print(os.path.abspath('.') )
# Query is it abs path or not
print(os.path.isabs('.'))

absPath = os.path.abspath('.')
print(os.path.dirname(absPath))
print(os.path.basename(absPath))

# Split the path into pieces
print(os.path.split( os.path.abspath('.') ) )
print(os.path.abspath('.').split(os.path.sep))

# Current file size
print(os.path.getsize( os.path.abspath('.') ) )

# Ls
print(os.listdir( os.path.abspath('.') ) )
for filename in os.listdir(os.path.abspath('.') ):
      print(filename)

# validation
print(os.path.exists("c:\\Users\\ffff"))
print(os.path.isfile(os.path.abspath('.')))
print(os.path.isdir(os.path.abspath('.')))


# File operation
helloFile = open(os.path.abspath('.') + os.path.sep + "ch1.py" , 'r')
# Can be either one off or seperate by line
# content = helloFile.read()
content = helloFile.readlines()
print(content)
helloFile.close()


# Write a test.txt with BasicModule world
helloFile = open(os.path.abspath('.') + os.path.sep + "test.txt", 'w')
helloFile.write ('Hello world!\n')
helloFile.close



















# The probleme here is
curDir = str(os.getcwd() + os.path.sep)
# Only work when all prefixed dir exist.
shutil.copy( curDir + "guests.py", curDir + "BasicModule" + os.path.sep + "guests.py")

# Copy folder
# Exception pop out when folder existed alr
shutil.copytree(curDir+"BasicModule", curDir+"hello2")


shutil.move( curDir+"hello2"+os.path.sep+"guests.py",  curDir+"updatedGuest.py")

#Not recomment to use as it delete content permanently
#os.Unlink(path) for delete file
#os.rmdir(path) remove empty dir
#os.rmtree(path) remove dir


#Safe deleye
import send2trash
#send2trash.send2trash('bacon.txt')
