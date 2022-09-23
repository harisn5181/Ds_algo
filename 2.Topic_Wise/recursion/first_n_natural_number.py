#we only need to concetrate on 3 things 1)base case ,2)hypotheseis  3) induction


#1 to n
"""def prints(n):
  if n==0:
    return 
  prints(n-1)
  print(n)
  return 

prints(10)
"""

#n to 1

def prints(n):
  if n==0:
    return 
  print(n)
  prints(n-1)

  

prints(5)