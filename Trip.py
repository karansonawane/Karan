n = int(input("enter no of students"))
while(n!=0 and n<1000):

    li = []
    s = 0
    total = 0
    for i in range(n):
        x = float(input("enter amount"))
        if(x<10000):
            li.append(x)
        else:
            print("excess amount")

    s=sum(li)
    avg = s / n
    for j in li:
        rem = avg - j
        if (rem >= 0):
            total = total + rem
    print("$%.2f" %(total))
    n=int(input("enter no of students"))
