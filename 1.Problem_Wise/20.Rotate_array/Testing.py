#Testing on 20 -09

arr=[1,2,3,4,5]
x=2
#arr=[3,4,5,1,2]
temp=[]
n=5
for i in range(x):
    temp.append(arr[i])

for i in range(n-x):
    arr[i]=arr[i+x]

for i in range(x):
    arr[n-x+i] =temp[i]

print(arr)
