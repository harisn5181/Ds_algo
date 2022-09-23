def last_index(arr,x,i=0):
    if len(arr) ==0:
        return -1
    last_i=last_index(arr[1:],x,i=i+1)

    if last_i !=-1:
        return last_i

    else:

        if arr[0]==x:
            return i
        else:
            return -1

arr=[1,2,4,3,4,4,5]
print(last_index(arr,4))