# ******************** Basics *********************

mystring = 'asdfghjkl'
print(mystring)

mystring = 'asdfghjkl'
print(mystring[3])

# ******************** Slicing *********************

# Biggining of slice

mystring = 'asdfghjkl'
print(mystring[3:])

mystring = 'asdfghjkl'
print(mystring[:3])

mystring = 'asdfghjkl'
print(mystring[2:5])


# Step Size

mystring = 'asdfghjkl'
print(mystring[::2])


# ******************** Methods *********************

# Upper

mystring = 'asdfghjkl'
x = mystring.upper()
print(x)

# Lower

mystring = 'asdfghjkl'
x = mystring.lower()
print(x)

# Split

mystring = 'asdfghjkl'
mystring2 = 'Hello World'
mystring3 = 'Hello World'
x = mystring.split()
y = mystring2.split()
z = mystring3.split('e')
print(x)
print(y)
print(z)


# ******************** Print Formating *********************

x = "Insert another string here: {}".format("INSERT ME!")
y = "Item One: {} Item Two: {}".format("dog","cat") 
z = "Item One: {y} Item Two: {x}".format(x = "dog", y = "cat") 
print(x)
print(y)
print(z)