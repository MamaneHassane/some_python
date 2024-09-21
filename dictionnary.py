# Dictionary : Key value pair
x = {'Key' : 4, 4 : 8, 'sam' : 'wayne'}
print(x)
print(x[4])
# You can just add
x['i exist now'] = 35
print(x)
# Delete using a key
del x['i exist now']
# Check the existence using the key
print('Key' in x) # True
print('sam' in x) # True
print('wayne' in x) # False
# Get the values in a list, because it returns a different datatype
print(list(x.values()))
# Get the keys in an array, because it returns a different datatype
print(list(x.keys()))
# Using for loop on the items
for key, value in x.items():
    print(key, '-->', value)
  
for key in x:
    print(key, '-->', x[key])