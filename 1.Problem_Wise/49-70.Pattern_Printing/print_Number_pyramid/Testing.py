#18-09

n=6
for i in range(n-1):

    for j in range(i):
        print(" ",end="") #4
    for k in range(i+1,n+1):
        print(k,end="") #6
    print()


#reverse


for i in range(n):

    for j in range(n-i-1):
        print(" ",end="")
    for k in range(n-i,n+1):
        print(k,end="") #6
    print()

