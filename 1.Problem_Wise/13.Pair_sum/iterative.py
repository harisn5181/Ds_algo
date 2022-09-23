arr=[2 ,8 ,10, 5, -2, 5]
count=0
len=len(arr)
Flag=False


for i in range(len):
  for j in range(len):
    if i ==j:
      continue
    if arr[i]+arr[j]== 10:
      print(i,j)
      count=count+1
      Flag=True

if Flag==True:
  print(count)
else:
  print("0")



#This is the correct Code
sum = 0
for i in range(n):
    j = i+1
    while j<n:
        if arr[i]+arr[j]==x:
            sum+=1
        j+=1
return sum

