def Multiplication(x,y):
    if y==0:
        return 0
    if x<y:
        return Multiplication(y,x)

    return x+Multiplication(x,y-1)


print(Multiplication(3,5))