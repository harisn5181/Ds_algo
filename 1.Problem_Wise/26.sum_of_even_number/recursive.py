#Brtueforce Apporach
#TC:0 (n) SC: 0 (1)

def sum_of_evennumber(n):
  global sum
  if n ==0 :
    return 
  if n ==1:
    return 
  sum_of_evennumber(n-1)
  if n %2 ==0:
    
    sum=sum+n
  return sum


sum=0
print(sum_of_evennumber(6))  