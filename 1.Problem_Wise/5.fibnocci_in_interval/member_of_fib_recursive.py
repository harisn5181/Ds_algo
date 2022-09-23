def fib_in_interval(fib0,fib1,n):

  if fib1>n:
    return
  if fib1==n:
    print("yes")
    

  fib=fib0+fib1
  fib0=fib1
  fib1=fib
 

  fib_in_interval(fib0,fib1,n)


#main
n=int(input())

fib_in_interval(0,1,n)
  