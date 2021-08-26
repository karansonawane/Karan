# Dictionaries

myStuff = {"key1":"value", "key2" : "value2"}
print(myStuff['key1'])
print(myStuff['key2'])

# Grabbing

myStuff = {"key1":"value", "key2" : "value2", "key3" : {'123':[1,2,'grabMe']}}
print(myStuff['key3']['123'][2])
print(myStuff['key3']['123'][2].upper())


myStuff2 = {'rose':'red', 'banana':'yellow'}
print(myStuff2['rose'])

myStuff3 = {'rose':'red', 'banana':'yellow'}
myStuff3['rose'] = 'pink'
myStuff3['watermelon'] = 'green'
print(myStuff3)

