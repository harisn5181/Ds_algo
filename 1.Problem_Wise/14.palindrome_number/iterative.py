



def checkPalindrome(n):
    
    
    real_num=n
    reverse_digit=0
    while(n >0):
      digit=n%10
      reverse_digit=reverse_digit*10 + digit
      n=n//10
    
    if real_num== reverse_digit:
        return True
    

	  
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
