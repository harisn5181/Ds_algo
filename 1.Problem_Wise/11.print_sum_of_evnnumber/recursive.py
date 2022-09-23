#Bruteforce approach

#TC:0 (n)  SC:0 (1)

def print_sum(n):
  global sum
  
  if n==1:
    return 

  print_sum(n-1)
 
  if n%2==0:
    sum=sum+n
  return sum 
sum=0
print(print_sum(10))

