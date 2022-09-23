
#Bruteforce Apporach 

#TC:0 (n)   SC:0 (1)
def fib_in_interval(fib0,fib1,n):

  
  if n==0 :
    print(fib1)
    return 
  
    

  fib=fib0+fib1
  fib0=fib1
  fib1=fib
 

  fib_in_interval(fib0,fib1,n-1)



#main
n=int(input())


if n<=0:
  print("we are expecting numbers from 1 to onwards")

elif n==1 or n==2 :
  print("1")
else:  
  fib_in_interval(1,1,n-2)


"""


fib=2
fib0=1
fib1=2



 3 2 1 


1 2 n=3

fib=3
fib0=2
fib1=3

fib_in_interval(2,3,n=2)

fib=5
fib0=3
fib1=5

fib_in_interval(3,5,n=1):
fib=8
fib0=5
fib1=8


fib_in_interval(5,8,n=0)


return """