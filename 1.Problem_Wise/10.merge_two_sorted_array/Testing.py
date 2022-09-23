#20-09

arr1=[1,3,5,7,9]
arr2=[2,4,6,8,10]
arr3=[]

arr1_index=0
arr2_index=0
for i in range(len(arr1)):
    if arr1[arr1_index]<= arr2[arr2_index]:
        arr3.append(arr1[arr1_index])
        arr1_index+=1
    else:
        arr3.append(arr2[arr2_index])
        arr2_index+=1
