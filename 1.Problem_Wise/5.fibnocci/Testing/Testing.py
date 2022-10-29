#nth fibnocci checking on 15-09

# 0 1 1 2 3 5 8

fib0=0
fib1=1
n=7
for i in range(n-2):
    fib=fib0+fib1
    fib0=fib1
    fib1=fib
print(fib)