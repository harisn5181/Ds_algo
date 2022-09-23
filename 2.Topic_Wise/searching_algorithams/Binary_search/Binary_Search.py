



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


arr=[1,2,3,4,5,6,7]
n=len(arr)
x=1
print(binarySearch(arr,n,x))