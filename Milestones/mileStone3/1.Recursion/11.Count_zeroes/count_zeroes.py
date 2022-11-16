
# digit=str(n)
# len=len(n)
# Flag=False


# for i in range(len-1):
#   in len == 1:
  
#   if i !=0:
#     Flag=True
  
# if Flag==True:  
#   print(digit[i])



# # # n=n+0

# # n=00123
# # print(n+0)



## Read input as specified in the question.
## Print output as specified in the question.
# Python implementation to count
# the occurrence of a digit in
# number using Recursion

# Function to count the digit K
# in the given number N



def countdigits(n, k):
  
	if n == 0:
   
   return 0
    
    
    
  
digit = n % 10
  digit=str(n)
  len=len(n)
  Flag=False
  
  
  if digit == k:
      
      
      for i in range(len-1):
        if len == 1:
           return 1 + countdigits(n / 10, k)

        if i !=0:
          Flag=True

      if Flag==True:  
           return 1 + countdigits(n / 10, k)
       
	
	return countdigits(n / 10, k)


n = int(input())

print(countdigits(n, 0))
