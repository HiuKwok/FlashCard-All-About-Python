
# dictionary ~ Map
# Compare two dict would return true as long as both contain same elements with keys.
myCat = {'size': 'fat',
         'color': 'gray',
         'disposition': 'loud'}

# Get key list
print(myCat.keys())

# Loop dictionary
# str( ) added as value not necessary to be string
for k, v in myCat.items():
    print('K: ' + k + ' V: ' + str(v))

# Bool : Check does dict contain such key
print('name' in myCat.keys() )

# Setdefault (Only insert when not exist)
myCat.setdefault('height', '15')
