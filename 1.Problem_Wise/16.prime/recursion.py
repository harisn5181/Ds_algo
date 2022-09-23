#Bruteforce approach 

"""


def prime(n,n_copy):
  global flag

  if n==1:
    return

  prime(n-1,n_copy)
  if n_copy %n ==0 :
    flag=True

  if flag==True:
    return False

  else:
    return True



#Main

n=int(input())
flag=False
n_copy=n
print(prime(n-1,n_copy))

"""



#2more optimized approach




# Python 3 Program to find whether
# a Number is Prime or Not using
# Recursion

# Returns true if n is prime, else
# return false.
# i is current divisor to check.
def isPrime(n, i = 2):

	# Base cases
	if (n <= 2):
		return True if(n == 2) else False
	if (n % i == 0):
		return False
	if (i * i > n):
		return True

	# Check for next divisor
	return isPrime(n, i + 1)


# Driver Program
n = 6
if (isPrime(n)):
	print("Yes")
else:
	print("No")
	
# This code is contributed by
# Smitha Dinesh Semwal
