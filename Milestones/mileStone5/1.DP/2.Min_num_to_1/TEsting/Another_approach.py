#ANOTHER WAY TO WRITE THIS PROGRAMMING WITHOUT USING GLOBAL VARIABLE CALLED COUNT ,BUT THIS CODE WILL NOT GIVE MIN LENGTH


def minstepst01(n):

    if n==1:
        return 0
    if n%3==0:
        c=minstepst01(n//3)
        return 1+c
    if n%2==0:
        c=minstepst01(n//2)
        return 1+c
    c=minstepst01(n-1)
    return 1+c

#MAIN
n=10
print(minstepst01(n))





