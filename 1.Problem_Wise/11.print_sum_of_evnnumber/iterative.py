#simple bruteforce 
# TC:0(n)   SC:0(1)

sum=0
n=10
for i in range(n+1):
  if i %2==0:
    sum=sum+i

print(sum)