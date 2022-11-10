import math
import sys

def minsquares(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0

    for i in range(1,n+1):
        ans=sys.maxsize
        root=int(math.sqrt(i))

        for j in range(1,root+1):
            
            currentans=1+dp[i-(j**2)]
            
            ans=min(ans,currentans)
        dp[i]=ans  
        temp="k"
    return dp[n]   
n=41
ans=minsquares(n)
print(ans)