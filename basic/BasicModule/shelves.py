import shelve





shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()) )
print(list(shelfFile.values()) )
if 'mydata' in shelfFile:
	print("Have some thing")
else:
	print ("None")
	cat = ['bass', 'code', 'coffee']
	shelfFile['mydata'] = cat

shelfFile.close()


#can write a custome module by this
import pprint
guests = [{'First' : 'Andy', 'Last' : 'Kwok'}, {'First' : 'Ken', 'Last' : 'Chan'}]
pprint.pformat(guests)
fileObj = open ('guests.py', 'w')
fileObj.write('Guests = ' + pprint.pformat(guests) + '\n')
fileObj.close()
