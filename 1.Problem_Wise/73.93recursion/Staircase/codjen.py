## Read input as specified in the question.
## Print output as specified in the question.
# Python program to find n-th stair
# using step size 1 or 2 or 3.

# Returns count of ways to reach n-th
# stair using 1 or 2 or 3 steps.


def findStep(n):
	if ( n == 0 ):
		return 1
	elif (n < 0):
		return 0

	else:
		return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)


# Driver code
n = int(input())
print(findStep(n))

# This code is contributed by Nikita Tiwari.

# 13, 2,2,   2,1,1  3,1,  1,2,1  1,2,2,  1,1,1,1