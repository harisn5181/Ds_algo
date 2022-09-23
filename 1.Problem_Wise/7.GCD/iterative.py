"""
#Bruteforce Apporach 1

def gcd(num1,num2):
  if num1<=num2:
    smallest=num1
  else:
    smallest=num2
  
  for i in range(1,smallest):
    if num1%i ==0 and  num2%i==0:
      gcd=i
  
  return gcd  


#main
num1=int(input())   
num2=int(input()) 

print(gcd(num1,num2))

"""


#Bruteforce Modified
def gcd(num1,num2):
  if num1<=num2:
    smallest=num1
  else:
    smallest=num2

  while smallest:
    if num1 % smallest == 0 and num2 % smallest == 0:
      break
    smallest=3


  return smallest
  



#main
num1=10
num2=20

print(gcd(num1,num2))

"""

#Lesson for me 


def gcd(num1,num2):
  if num1<=num2:
    smallest=num1
  else:
    smallest=num2
    
  ans = 0
  for i in range(2,smallest):
    if num1%i ==0 & num2%i==0:
      ans = i
      break
  
  return ans  



#main
num1=100
num2=40

print(gcd(num1,num2))"""


