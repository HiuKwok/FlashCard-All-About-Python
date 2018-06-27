import csv

# Read from file, plz comment out read part if file is not present
exampleFile = open('output.csv')
exampleReader = csv.reader(exampleFile)


# #Whole thing
exampleData = list(exampleReader)
print(exampleData)
# Selected field
print(exampleData[0][1])

# For loop
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))




# Write
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
# Custome delimitor
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()