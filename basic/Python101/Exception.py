import traceback
# Manually raise a exception
def printEx():
    raise Exception ('Hello exception')


try:
    printEx()
except Exception as err:
    print('Anexception happened: ' + str(err))


# Traceback
try:
    raise Exception('Hello exception')
except:
    print(traceback.format_exc())
