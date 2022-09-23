"""

 
Output we need 

1
11
202
3003

1          
11
121
1221

"""
def support_function(j,n):
  if j > n:
    return 
    
  if j==1 or j == n:

  
    print(n-1,end="")

  else:
    print("0",end="")
  support_function(j+1,n)




  

def Number_pattern2(n):
  if n ==1:
    print("1")
    
    return
  Number_pattern2(n-1)
  j=1
  support_function(j,n)
  print()
  


#Main
n=int(input("input number:"))
Number_pattern2(n)


"""


dry run

j=1
support function (n=3,j=1)
def support function(n,j):
  if j > n:
    return 
    
  if j==1 or j == n:

  
    print("1",end="")

  else:
    print("2",end="")




  j=j+1
"""