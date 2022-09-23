while True:
    n=int(input("What operation you want to perform "))
    if n<6:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))

    if n==1:
        a=a+b
    if n==2:
        a=a-b
    if n==3:
        a=a*b
    if n==4:
        a=a/b
    if n==5:
        a=a%b
    if n==6:
        print("programm stopped")
        break
    else:
        print("you give a invalid operation ")
    print(a)