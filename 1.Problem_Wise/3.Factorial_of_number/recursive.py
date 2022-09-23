#Bruteforce Approach
#TC:0(n)  SC:0(1)


def fact(n):
   
  if n==1:
    return 1
  return n*fact(n-1)
  
  
#Main

n=int(input())
if n<0:
  print("no factorial for number less than 0")
if n==0:
  print(1)
if n>=1:
  
 print(fact(n))

