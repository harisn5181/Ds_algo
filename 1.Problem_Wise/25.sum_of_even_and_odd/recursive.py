#Bruteforce  TC:0 (n)   SC:0 (1)
"""
def sum_of_evenand_odd(n):
  global even 
  global odd

  if n <=0:
    return
  digit=n%10

  if digit %2 ==0:
    even=even+digit
  else:
    odd=odd+digit

  sum_of_evenand_odd(n//10)
  return  (even,odd)

#Main 
even,odd=0,0
n=int(input("enter number"))
even,odd=sum_of_evenand_odd(n)
print(even,odd)
"""
def sum_of_evenand_odd(n,even=0,odd=0):

  if n <=0:
    print(even,odd)
    return


  if n %2 ==0:
    even=even+n
  else:
    odd=odd+n

  sum_of_evenand_odd(n-1,even,odd)
#1,2,3,4,5,6,7,8,9,10

#Main

n=10
sum_of_evenand_odd(n)
