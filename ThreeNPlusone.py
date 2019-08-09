
i=int(input("enter the number"))
j=int(input("enter the number"))
if(i>j):
    i,j=j,i
c=0
def prob(i,j,c):
    if(i<0 or j<0):
        print("invalid input")
    else:
        for n in range(i, j + 1):
            a = []
            a.append(n)
            while (n > 1):

                if (n % 2 == 0):
                    n = n // 2
                    a.append(n)

                else:
                    n = 3 * n + 1
                    a.append(n)

            if (len(a) > c):
                c = len(a)

        print(i, j, c)


prob(i,j,c)