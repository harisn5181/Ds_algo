"""

i am getting append    
		if arr[i] != arr[i+1]: error ,i should ask on ta

  
def findUnique(arr, n) :
    #Your code goes here
    
  arr.sort()
    
	for i in range(n):
        
		if arr[i] != arr[i+1]:
            
            if i== (n-1):
                return arr[i]
            if arr[i] != arr[i+2]:
                
            	return arr[i]
            else:
                return arr[i+1]
"""



def findUnique(arr,n):
  arr.sort()
  if n%2!=0:
      
    for i in range(0,n,2):
      if i ==(n-1):
        return arr[i]
      if arr[i] != arr[i+1]:
        
        if arr[i] != arr[i+2]:
          return arr[i]
        else:
          return arr[i+1]

print(findUnique([3,4,9,7,3,4,7],7))




