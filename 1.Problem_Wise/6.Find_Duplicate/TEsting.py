arr=[0,1,0,2,3]
arr.sort()
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        print(arr[i])
