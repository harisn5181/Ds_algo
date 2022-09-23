#ANOTHER WAY TO WRITE THIS PROGRAMMING WITHOUT USING GLOBAL VARIABLE CALLED COUNT ,BUT THIS CODE WILL NOT GIVE MIN LENGTH

import sys



def minstepst01(n):
    global count
    if n==1:
        return 0

    if n%3==0:
        count = count + 1
        minstepst01(n//3)

        return
    if n%2==0:
        count = count + 1
        minstepst01(n//2)

        return
    count = count + 1
    minstepst01(n-1)

    return
#MAIN

n=10
count=0
minstepst01(n)

print(count)



