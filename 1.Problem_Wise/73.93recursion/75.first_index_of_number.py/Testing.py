#

def first_index_of_array(arr,x,i=0):
    if len(arr)==0:
        return -1

    if arr[0]==x:
        return i

    return first_index_of_array(arr[1:],x,i=i+1)



arr=[1,2,3,4,5]
print(first_index_of_array(arr,6))