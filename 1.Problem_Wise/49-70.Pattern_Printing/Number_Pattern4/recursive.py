"""
Output

1234
123
12 
1

"""

def support_function(n):
  if n ==0:
    return
  support_function(n-1)
  print(n,end="")


def Num_pattern4(n):
  if n ==0:
    return
  Num_pattern4(n-1)
  support_function(n)
  print()



#Main
n=int(input("Enter number:"))
Num_pattern4(n)