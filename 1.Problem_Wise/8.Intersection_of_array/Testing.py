import sys

arr1=[2, 6, 8, 5, 4, 3]

arr2=[2, 3, 4, 7]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr1[i])
            arr2[j]=sys.maxsize