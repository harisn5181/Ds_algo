

arr1=[2,6,1,4,2,4]
arr2=[1,2,3,2,4,5]

len1=len(arr1)
len2=len(arr2)



for i in range(len1):
  for j in range(len2):
    if arr1[i]==arr2[j]:
      print(arr1[i])
      break