




import sys
sys.setrecursionlimit(10000)
def fib(n):
  if n==1 or n==2:
    return 1
  fib1=fib(n-1) 
  fib2=fib(n-2)
  output=fib1+fib2
  return output 

print(fib(7))