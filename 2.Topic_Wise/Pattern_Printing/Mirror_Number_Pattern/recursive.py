#Bruteforce Apporach TC: 0(n^3)   SC:0 (1)


def put_number(n):
  if n==0:
    return
  put_number(n-1)
  print(n,end="")

def put_spaces(n):
  if n ==0:
    return 
  put_spaces(n-1)
  print(" ",end="")
  

def mirror_number_pattern(n,n_copy):
  if n==0:
    return
  mirror_number_pattern(n-1,n_copy) #get all 4 rows   
  put_spaces(n_copy-n)   # put spaces for each row
  put_number(n)               #put numbers 
  print()                    #put spaces


#Main
n=int(input("Enter number for recursion"))
n_copy=n
mirror_number_pattern(n,n_copy)



