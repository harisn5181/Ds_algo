def checkPalindrome(num):
  
  str_num=str(num)
  length=len(str_num)
  temp=num
  sum=0
  while (temp>0):
    rem=temp%10
    
    sum= sum+rem**length


    temp=temp//10

    
  

  
 
  if sum==num:
    return True
  
	
	
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
