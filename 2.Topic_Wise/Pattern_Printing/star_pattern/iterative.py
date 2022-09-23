"""
#Output


   *
  ***
 *****  
*******

"""
#Bruteforce Apporach
#TC: is it 0 (n^3)  SC:0 (1)
#Code


n = int(input())
i = 1
k=1

def star_pattern():
  global i 
  while i <= n :
      spaces = 1
      while spaces <= n - i :    #is it o (n)
          print(' ', end = '')
          spaces = spaces + 1
      
      j = 0
      global k  
      for j in range(k):        #is it 0 (n)
      
           print("*", end = '')
           j = j + 1
      print()
      i = i + 1
      k=k+2
star_pattern()    
    

"""Dry run


n=4
i=1
while( 1<= 4):
  spaces=1
  while 1<= 3:
    print()
    spaces2

    
"""
