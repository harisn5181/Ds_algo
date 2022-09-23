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