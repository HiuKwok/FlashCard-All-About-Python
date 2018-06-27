
# Array
spam = ['cat', 123.546, 'Andy', 77858, True]
# Access array member one by one
for i in range(0, len(spam)):
    print(spam[i])

# Array IO process
subSpam = spam[1:2]
subSpam = subSpam + spam
subSpam.append('BasicModule')
subSpam.insert(1, 'world')
subSpam.remove('BasicModule')
