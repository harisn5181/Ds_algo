#18-09
arr=[2 ,8 ,10, 5, -2, 5,10]
count=0
for i in range (len(arr)):
    for j in range( i+1,len(arr)):
        if arr[i]+arr[j] ==10:
            count=count+1

print(count)