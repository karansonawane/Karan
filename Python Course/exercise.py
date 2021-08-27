s = 'django'
print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])


mylist = [1,1,1,2,2,2,3,3,3,4,4,4]
print(set(mylist))


x = "Hello my dog's name is {name} and he is {age} years old".format(name = 'Sammy', age = 4)
print(x)