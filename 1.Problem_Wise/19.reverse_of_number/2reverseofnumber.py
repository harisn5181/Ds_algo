


n=int(input()) #for taking reverse of element
reverse_digit=0
while(n >0):
    digit=n%10
    reverse_digit=reverse_digit*10 + digit
    n=n//10
    
print(reverse_digit)    
    