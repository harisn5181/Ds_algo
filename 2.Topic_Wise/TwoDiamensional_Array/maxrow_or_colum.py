input=[[6,9],[8,5],[9,2]]

#column sum 
n=2
m=3
max_sum,index=-222222222,0
for i in range(n):
  sum=0
  for j in range(m):
    sum=sum+input[j][i]
  if sum> max_sum:
    max_sum=sum
    index=i

print(index  ,  max_sum)

#row sum
max_sum_c,index=-222222222,0
for i in range(m):
  sum=0
  for j in range(n):
    sum=sum+input[i][j]
  if sum> max_sum_c:
    max_sum_c=sum
    c_index=i

print(c_index  ,  max_sum_c)

if max_sum_c>max_sum:
  print(max_sum_c, c_index)
else:
  print(max_sum,index)



#code from ta
  
arr=[[6,9],[8,5],[9,2]]
rmax=-2147483648
n=2
m=3
r_index=0
for row in arr:
    sum=0
    for i in row:
        sum+=i
    if sum>rmax:
        rmax=sum
        r_index=arr.index(row)
cmax=-2147483648
c_index=0
for c in range(mCols):
    sum=0
    for r in range(nRows):
        sum+=arr[r][c]
    if sum>cmax:
        cmax=sum
        c_index=c

if rmax>=cmax:
    print("row",r_index,rmax)
else:
    print("column",c_index,cmax)