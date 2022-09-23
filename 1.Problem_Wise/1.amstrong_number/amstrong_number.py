# # Check Armstrong
# Send Feedback
# Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
# For example,

# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

# Input Format :

# Integer n

# Output Format :

# true or false

# Sample Input 1 :

# 1

# Sample Output 1 :

# true

# Sample Input 2 :

# 103

# Sample Output 2 :

# false




def checkPalindrome(num):
  pass
  temp=num
  sum=0
  while (temp>0):
    rem=temp%10
    
    sum=sum+(rem*rem*rem)


    temp=temp//10

    
  

  
 
  if sum==num:
    return True
  
	
	
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')




#more beeter apporach considering for all number of lengths of strings

n = int(input())
sum=0
order=len(str(n))
m=n
while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
if(sum==m):
    print("true")
else:
    print("false")