#Bruteforce approach
#TC: 0 (n)  SC: 0 (1)

def print_evennumber(n):
  if n == 1:
    return 

  print_evennumber(n-1)
  if n %2==0:
    print(n)

n=10
if n<=1:
  print("nothing")
else:
  print_evennumber(n)
"""  
9
8  8
7 
6 6 
5
4  4
3  
2  1
"""
