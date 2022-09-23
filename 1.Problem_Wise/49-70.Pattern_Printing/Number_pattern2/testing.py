
"""

1
11
202
3003


print(1)
n=4

for i in range(1,n):
    j=0
    while j<=i:
        if j==0 or j==i:
            print(i,end="")

        else:
            print(0,end="")
        j=j+1

    print()
"""


#recursion
"""
def secondloop(n,j,n_orginal):

    if n==0:
        return

    secondloop(n-1,j-1,n_orginal)
    if j==1 or j== n_orginal:
        print(n_orginal-1,end="")
    else:
        print(0,end="")


def patter2(n):
    if n==1:
        return
    patter2(n-1)
    secondloop(n,n,n)
    print()

print(1)
patter2(4)
"""