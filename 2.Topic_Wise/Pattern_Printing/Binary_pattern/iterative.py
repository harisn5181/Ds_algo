"""
output

1111
000
11
0



"""

n=int(input())
for i in range(0,n):

  for c in range(n-i,0,-1):
    j=i+1
    if j %2!=0:
      print(1,end="")
    else:
      print(0,end="")
      
  print()  
        