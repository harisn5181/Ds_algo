
#15-09
"""
Dry run
  *
 ***
*****
 ***
  *

  """

i=0
n=2
while i<= n:
    for i in range(n-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    i=i+1
