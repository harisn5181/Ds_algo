#Bruteforce approach 
#TC:0 (n)   SC:0 (1)



def sum(n):
  if n <=0:
    return 
  if n==1:
    return 1
  return n+sum(n-1)
  

  
print(sum(0))


