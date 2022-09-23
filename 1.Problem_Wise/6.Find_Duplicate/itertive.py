
#Without Function

# arr=[0,1,0,2,3]
# len=len(arr)
# # arr.sort()

# for i in range  (0,len-1): 
#   if arr[i]== arr[i+1]:    
#     print(arr[i+1])



# arr.sort()

# for i in range  (0,len-1):
  
      
#     if arr[i]== arr[i+1]:
          
#       print( arr[i+1])
#       break



# #Function Based



def duplicateNumber(arr, n):
  arr.sort()
  for i in range  (0,n-1):
    if arr[i]== arr[i+1]:    
      return (arr[i+1])
      

 


arr=[0,1,2,3,3]
n=len(arr)
print(duplicateNumber(arr,n))



