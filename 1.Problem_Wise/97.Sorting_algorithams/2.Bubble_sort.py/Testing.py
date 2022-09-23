#Testing on 20-09

#Bubble sort

arr=[8,5,3,1]
n=len(arr)
for i in range(len(arr)-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
#arr=[1,3,5,8]
