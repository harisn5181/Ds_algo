#testing on 15-09

"""
Dry run for print fibnocci upto a variable using iteration
10
0 1 1 2 3 5 8


n=10
fib0=0
fib1=1
print(fib0,end=" ")
print(fib1,end=" ")

for i in range(10):
    fib=fib0+fib1 #13
    fib0=fib1 # 5
    fib1=fib#8
    if fib<=n:
        print(fib,end=" ")


#Dry run for print fibnocci upto a variable using recursion



def fibnocci(n,fib0,fib1): #,0,1,1,2,3


    fib=fib0+fib1 # 3
    if fib > n:
        return

    print(fib,end=" ")
    fibnocci(n,fib1,fib)#10,2,3

n=10
fib0=0
fib1=1
print(fib0,end=" ")
print(fib1,end=" ")

fibnocci(n,fib0,fib1)


#Dry run for print fibnocci for 10 numbers using iteration


#0 1 1 2 3 5 8


n=7
fib0=0
fib1=1
print(fib0,end=" ")
print(fib1,end=" ")

for i in range(n-2):
    fib=fib0+fib1
    fib0=fib1
    fib1=fib
    print(fib,end=" ")


#Dry run for print fibnocci for 10 numbers using recursion



def fibnocci(n):
    if n==2:
        fib0 = 0
        fib1 = 1
        print(fib0, end=" ")
        print(fib1, end=" ")
        return fib0,fib1
    fib0,fib1=fibnocci(n-1)
    fib=fib0+fib1
    print(fib,end=" ")
    return fib1,fib

fibnocci(7)
