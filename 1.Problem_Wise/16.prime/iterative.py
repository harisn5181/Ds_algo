#Bruteforce TC: 0(n)   SC: 0 (1)




def prime(n):
  
  Flag=False
  for i in range(2,n):
    
    if n%i==0:
      Flag=True
      break
  if Flag==False:
    print("prime number")

  else:
    print("not a prime number")

#Main
n=int(input())
prime(n)