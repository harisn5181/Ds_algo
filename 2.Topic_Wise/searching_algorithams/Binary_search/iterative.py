
from sys import stdin


def binarySearch(arr, n, x) :
  
    #Your code goes here
    l=0
    search=x
    h=n-1
    mid=0
   
    
    while (l<=h):
      
      
      mid=(l+h)//2
      if arr[mid]==search:
        
          return mid
      elif x<arr[mid]:
          h=mid-1
      else:
          l=mid+1
            
    return -1     
        
        























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1