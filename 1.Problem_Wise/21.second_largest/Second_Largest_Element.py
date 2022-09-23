arr=[9]
n=len(arr)
if n>1:
  for i in range(n-1):
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1] , arr[j]
      
  print( arr[-2])