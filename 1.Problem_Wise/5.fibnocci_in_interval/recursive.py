#bruteforce approach
#TC: 0 (unknown)    SC:0 (n)

def fib_in_interval(fib0,fib1,n):

  if fib1>n:
    return
  fib_ser.append(fib1)

  fib=fib0+fib1
  fib0=fib1
  fib1=fib
 

  fib_in_interval(fib0,fib1,n)
  return fib_ser


#main
n=int(input())
fib_ser=[0]
print(fib_in_interval(0,1,n))
  