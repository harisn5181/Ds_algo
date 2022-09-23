"""
Dry run

4444
333
22
1


n=4
for i in range(n):
    for j in range(n-i):
        print( n-i,end="")
    print()

"""

#Recursive
def helper(n,n_orginal):
    if n==0:
        return
    print(n_orginal,end="")
    helper(n-1,n_orginal)


def pattern(n):
    if n ==0 :
        return
    helper(n,n)
    print()
    pattern(n-1)


pattern(4)




