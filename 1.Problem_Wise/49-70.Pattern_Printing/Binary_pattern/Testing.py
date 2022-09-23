#18-09

n=6
for i in range(n):

    for j in range(i):
        print(" ",end="") #4
    for k in range(i+1,n+1):
        print(k,end="") #6
    print()
print(j)
print(k)

