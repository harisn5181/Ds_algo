
def firstIndex(arr, x,index):
    if len(arr) ==0:
        return -1
    if arr[0] == x:
        return index
    return firstIndex(arr[1:],x,index+1)
    
    
        
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
index=0

print(firstIndex(arr, x,index))