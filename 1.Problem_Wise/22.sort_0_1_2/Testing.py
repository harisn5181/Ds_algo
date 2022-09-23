#18-09


arr=[0, 1, 1 ,0 ,1, 0, 1]
#arr=[0, 0, 0 ,1 ,1, 1, 1]

for i in range(len(arr)):
    if arr[i]==0:
        for j in range(i):
            if arr[j]==1:
                arr[i],arr[j]=arr[j],arr[i]
print(arr)