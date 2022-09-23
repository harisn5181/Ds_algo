# input=[[122,2,3,4111],[3,4,5,4],[5,6,7,42]]
# n=4
# m=3
# max_sum,index=0,0
# for i in range(n):
#   sum=0
#   for j in range(m):
#     sum=sum+input[j][i]
#   if sum> max_sum:
#     max_sum=sum
#     index=i

# print(index  ,  max_sum)


li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for j in range(4):
    for ele in li:
        print(ele[j],end = "")