import math
import sys








def minsquare(n):

    if n ==0:
        return 0

    ans=sys.maxsize

    root=int(math.sqrt(n))

    for i in range(1,root+1):
        currAns=1+minsquare(n-(i**2))
        ans=min(ans,currAns)

    return ans


n=4
ans=minsquare(n)
print(ans)


