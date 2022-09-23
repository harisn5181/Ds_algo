"""
Output

  *
 ***
*****
 ***
  *

  
"""

def Daimond_star_pattern(n):
  global star_count
  spaces=n//2
  temp_spaces=spaces

  
  for i in range(n//2):
    for i in range(spaces,0,-1):
      spaces=spaces-1
      print(" ",end="")

    for i in range(star_count):
      print("*",end="")


    star_count+=2
    temp_spaces=temp_spaces-1
    spaces=temp_spaces
    print()

  
  for i in range(n):
    print("*",end="")
  print()  


  star_count=star_count-2
  global spaces_reverse 
  for i in range(n//2):

    for i in range(spaces_reverse):
      print(" ",end="")


    
    for i in range(star_count):
      print("*",end="")

    print()
    star_count=star_count-2
    spaces_reverse+=1
  
  # for i in range(n//2):
  #   for i in range(spaces,0,-1):
  #     spaces=spaces-1
  #     print(" ",end="")

      
    




  



  





n=9
spaces_reverse=1
star_count=1
Daimond_star_pattern(n)