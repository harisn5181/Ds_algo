
arr=[1,1,2,0,3,4]
for i in range(len(arr)):
  if i!=0:
    for j in range(0,i):
      print(i,j)
      if arr[j]==0:
        
        arr[i],arr[j]=arr[j],arr[i]

print (arr)
