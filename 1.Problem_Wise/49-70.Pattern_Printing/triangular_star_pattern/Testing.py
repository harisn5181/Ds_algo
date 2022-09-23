"""
Dry run
patter number 4
*
**
***
****


for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()
    """
#using recursion

def pattern(n):
    if n==0 :
        return
    pattern(n-1)
    pattern(n-1)
    print("*",end="")


pattern(3)


