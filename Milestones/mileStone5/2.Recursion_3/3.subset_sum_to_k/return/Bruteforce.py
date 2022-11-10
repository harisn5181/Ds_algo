# we are using array copy inorder to get the orginal size of the array,we can also do that by passing a arguement for that






def subsetssum(intialarray,arr,k):
    if len(arr)==0:
        li=[]
        return li
        
    li=subsetssum(intialarray,arr[1:],k)
    
    if arr[0] == k:
        li.append(arr[0])

    for i in range (intialarray-len(arr)):
        if arr[0]+copy_arr[i]==k:
            li.append((arr[0],copy_arr[i]))
    return li 

arr=[5 ,3 ,3, 17, 1, 3]
copy_arr=arr.copy()
li=subsetssum(len(arr),arr,1)
print(li)
