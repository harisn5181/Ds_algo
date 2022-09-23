
# def selection_sort(arr,n):
  
#   for i in range(n):
  
    
#     min=i
#     Flag=False
#     for j in range(i+1,n):
#       if arr[min] > arr [j] :
#         min=j
#         Flag=True
        
#     if Flag==True:
#       arr[i], arr[min] = arr[min],arr[i]
      
      
      
      

#   return (arr)
# arr=[13,8,2,4,5]
# n=len(arr)
# print(selection_sort(arr,n))





# # Python program for implementation of Selection
# # Sort
# import sys
# A = [64, 25, 12, 22, 11]
 
# # Traverse through all array elements
# for i in range(len(A)):
  
#  # Find the minimum element in remaining
#  # unsorted array
#  min_idx = i
#  for j in range(i+1, len(A)):
#   if A[min_idx] > A[j]:
#    min_idx = j
    
#  # Swap the found minimum element with
#  # the first element  
#  A[i], A[min_idx] = A[min_idx], A[i]
 
# # Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#  print("%d" %A[i]),








def selection_sort(arr,n):
  
  for i in range(n):
  
    
    min=i
    Flag=False

    j=i+1
    
    while (j<n):
   
      if arr[min] > arr [j] :
        min=j
        Flag=True
      j=j+1
        
    if Flag==True:
      arr[i], arr[min] = arr[min],arr[i]
      
      
      
      

  return (arr)
arr=[13,8,2,4,5]
n=len(arr)
print(selection_sort(arr,n))


