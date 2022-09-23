

"""
Dry run


123456    1  0   n-i =0  
  23456   2  2    
    3456  3  4
      456
        56
          6
        56     n-2= 6-1
      456           6-2
    3456
  23456
123456




"""
n=int(input())
spaces=0

for i in range(1,n+1):
 k=0

 while k<spaces:
   print(" ",end="")
   k=k+1

 for k in range(i,n+1):
   print(k,end="")
   

 spaces=spaces+2  
 print()  

  
spaces=spaces-4

for i in range(1,n):
 k=0

 while k<spaces:
   print(" ",end="")
   k=k+1

 for k in range(n-i,n+1):
   print(k,end="")
   

 spaces=spaces-2  
 print()  