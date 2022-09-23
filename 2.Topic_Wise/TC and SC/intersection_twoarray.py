n=4
m=4
arr1=[1,2,3,3]
arr2=[3,4,5,3]
for i in range(n):
        for j in range(m):
            if arr1[i] ==arr2[j]:
                print(arr1[i])
                arr2[j]=-22222222222
                break
