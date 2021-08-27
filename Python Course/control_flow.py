# ****************** Comparison Operator *****************

# Greater Than
2 > 1

# Less Than
1 < 2

# Greater than or equal to
1 >= 1

# Less than or equal to
1 <= 2

# Equality
1 == 1
1 == "1"
'hi' == 'bye'

# Inequality
1 != 2


# ****************** Logical Operator *****************

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operator
(1 == 2) or (2 == 3) or (4 == 4)



# ****************** if Statement *****************
if 1 < 2:
    print('yes!')


if 1 < 2:
    print("First block")
    if 20 < 3:
        print("Second block")    


# ****************** if else Statement *****************
if 1 < 2:
    print("hello")
else:
    print("last")    


# ****************** elif Statement *****************
if 1 > 2:
    print("hello")
elif 3 == 3:
    print("elif run") 
else:
    print("last") 