def arrayRotateCheck(arr, n):
    #Your code goes here
    min=0
    for i in range(1,n):
        if arr[i]<arr[min]:
            min=i
    return (min)



arr=[5 ,6 ,1 ,2 ,3 ,4]
n=len(arr)
print(arrayRotateCheck(arr,n))