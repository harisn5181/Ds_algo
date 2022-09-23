"""

1
21
321
4321
"""

n=4
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()