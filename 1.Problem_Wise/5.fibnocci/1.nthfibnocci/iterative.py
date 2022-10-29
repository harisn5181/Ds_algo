n=int(input())
fib0=1
fib1=1
Flag=False

if n==1 or n ==2 :               
    print(1)

else:
    for i in range(n-2):
        fib=fib0+fib1 # 3 
        fib0=fib1 # 2
        fib1=fib # 3
        Flag=True  
if Flag==True:
    print(fib) 



