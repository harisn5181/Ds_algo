# Remember this division
#number=10
#print(number//2)




## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)


number=int(input()) #for taking input

even_sum=0
odd_sum=0

    
while(number>0):
    rem=number%10
    
    
    if rem %2==0:
        even_sum=even_sum+rem
    else:
        odd_sum=odd_sum+rem
    
    number=number//10
print(even_sum ," " ,odd_sum)        