"""

   1
  212
 32123
4321234
"""
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i,1,-1):
        print(k,end="")
    for h in range(1,i+1):
        print(h,end="")
    print()