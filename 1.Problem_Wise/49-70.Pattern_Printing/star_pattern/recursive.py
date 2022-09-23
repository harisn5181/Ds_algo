#Bruteforce Apporach TC: 0(n^3)   SC:0 (1)
"""
Output=
   *
  ***
 *****  
*******

"""

def put_number(n):
  
  if n==0:
    return
  put_number(n-1)
  print("*",end="")

def put_spaces(n):
  if n ==0:
    return 
  put_spaces(n-1)
  print(" ",end="")
  

def mirror_number_pattern(n,n_copy):
  global number_global 
  if n==0:
    return
  mirror_number_pattern(n-1,n_copy) #get all 4 rows   
  put_spaces(n_copy-n)  
  
  # put spaces for each row
  number_global=number_global+2
  put_number(number_global)               #put numbers 
  print()                    #put spaces


#Main
n=int(input("Enter number for recursion"))
n_copy=n
number_global=-1
mirror_number_pattern(n,n_copy)
