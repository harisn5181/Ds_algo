"""

Output





   1           
  212           n-2=4-2=2
 32123          4-3=1
4321234         n-4  





"""

n=int(input())

#rows

print("   1")
n_columns=3
spaces=2
for i in range(2,n+1):
  j=0
  position_1=n//2

  for x in range(n-spaces):
    print(" ",end="")

  
  for c in range(n_columns):
    
    if j ==0 :
      print(i,end="")
      j=j+1
  
    elif j<position_1: 
      for k in range(i-1,0,-1):
        print(k,end="")

      j=position_1+1  
        
    # elif j==n//2:
    #   print("1",end="")
    #   j=j+1
  
    elif j>position_1:
      
      for l in range(2,i+1):
        print(l,end="")
      break  
        
  print()  
  spaces=spaces+1
  n_columns+=2
   
    
  
  
  
  