def put_numbers(n):
  for i in range(n):
    print(i+1,end="")

def put_spaces(n):
  for i in range(n):
    print(" ",end="")


def put_numbers_reverse(n):
  for i in range(n,0,-1):
    print(i,end="")


  
def recursive(n,n_copy):
  if n==0 :
    return
  recursive(n-1,n_copy)
  put_numbers(n)
  put_spaces(n_copy-n)
  put_spaces(n_copy-n)
  put_numbers_reverse(n)
  print()



#Main
n=int(input("enter number:"))
n_copy=n
recursive(n,n_copy)