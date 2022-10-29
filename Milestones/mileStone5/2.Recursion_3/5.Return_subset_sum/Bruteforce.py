arr=[5, 12 ,3 ,17, 1, 18 ,15 ,3, 17 ]
copy_arr=arr.copy()



def subsetssum(copy_arr,arr,k):
    if len(arr)==0:
        return
    subsetssum(copy_arr,arr[1:],k)

    for i in range (len(copy_arr)-len(arr)):
        if arr[0]+copy_arr[i]==k:
            print(arr[0],copy_arr[i])

subsetssum(copy_arr,arr,6)