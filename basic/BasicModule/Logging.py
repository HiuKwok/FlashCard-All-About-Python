# Logging
import logging

# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# Log to file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Hello log')
# Disable log
logging.disable(logging.DEBUG)
