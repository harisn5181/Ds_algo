def lastIndex(arr,x,si):
    
    
    l=len(arr)
    if si == l:
        return -1
    y=lastIndex(arr,x,si+1)
    if y!=-1:
        return y
    else:
        if arr[si]==x:
            return si
        else:
            return -1
        
        
        
from sys import setrecursionlimit
setrecursionlimit(10000000)
n=int(input())
arr=list(map(int,input().split()))
x=int(input())
print(lastIndex(arr,x,0))
