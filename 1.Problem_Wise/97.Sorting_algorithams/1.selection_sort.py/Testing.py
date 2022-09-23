"""# #20-09
#
# arr=[20,10,3,4,8,1,2,100,12]
# #[3, 4, 8, 20, 12, 10]
# n=6
#
# for i in range(n):
#     smallest=i
#
#     for j in range(i+1,n):
#         if arr[j]<arr[smallest]:
#             smallest=j
#
#
#     arr[i],arr[smallest]=arr[smallest],arr[i]
#
# print(arr)
"""

li=[20,10,3,4,8,1,2,100,12]
for i in range(0,len(li),1):
        min=i
        for j in range(i+1,len(li),1):
            if(li[min]>li[j]):
                min=j
        li[i],li[min]=li[min],li[i]
print(li)