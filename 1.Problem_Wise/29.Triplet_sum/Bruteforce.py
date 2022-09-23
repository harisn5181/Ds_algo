arr=[1,2,3,4,5,6,7]
count=0
X=12
for i in range(7):
  for j in range(i+1,7):
    for k in range(j+1,7):
      if arr[i]+arr[j]+arr[k]==X:
        
        count=count+1

        #print(arr[i],arr[j],arr[k])
        
print(count )