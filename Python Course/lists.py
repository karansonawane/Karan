# Lists

mylist1 = [1,2,3,4]
mylist2 = ['stringasdfg',1,2,3,4,5,'asdf',[1,2,3,4]]
print(len(mylist1))
print(mylist2)

# ********************** Indexing and Slicing ************************

# Indexing

mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist[2])

# Slicing

mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist[2:])
print(mylist[:2])
print(mylist[2:4])

# ********************** Reassignment ************************

mylist3 = ['a', 'b', 'c', 'd', 'e']
print("before reassignment")
print(mylist3)
mylist3[0] = 'NEW ITEM'
print("after reassignment")
print(mylist3)

# *************************************************************

#.append

mylist4 = ['a', 'b', 'c', 'd', 'e']
mylist4.append("NEW ITEM")
print(mylist4)

# .extend

mylist5 = ['a', 'b', 'c', 'd', 'e']
listtwo = ['x', 'y', 'z']
mylist5.extend(listtwo)
print(mylist5)

# Remove from list .pop

mylist6 = ['a', 'b', 'c', 'd', 'e']
item = mylist6.pop()
item2 = mylist6.pop(0)
print(mylist6)
print(item)
print(item2)

# reverse

mylist7 = ['a', 'b', 'c', 'd', 'e']
mylist7.reverse()
print(mylist7)

# Sort

mylist8 = [1, 2, 6, 56, 4, 98, 70, 40]
mylist8.sort()
print(mylist8)


# nested list

mylist9 = [1, 2, ['x', 'y', 'z']]
print(mylist9[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)