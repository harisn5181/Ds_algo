"""

Output

1        1
12      21
123    321
1234  4321
1234554321


Dry run """
n=4
for i in range(1,n+1):

    for j in range(i):
        print(j+1,end="")

    for k in range((n-i)*2):
        print(" ",end="")
    for x in range(i,0,-1):
        print(x,end="")
    print()
