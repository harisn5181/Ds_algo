import math
import sys


def minsquare(n,dp):
    if n ==0:
        return 0
    ans=sys.maxsize
    root=int(math.sqrt(n))
    for i in range(1,root+1):
        newCheckvalue=n-(i**2)
        if dp[newCheckvalue] ==-1:
            smallans=minsquare(newCheckvalue,dp)
            dp[newCheckvalue] =smallans
            currans=1+smallans
        else:
            currans= 1+dp[newCheckvalue]
        ans=min(ans,currans)
    return  ans

n=int(input())
dp=[-1 for i in range (n+1)]
ans=minsquare(n,dp)
print(ans)