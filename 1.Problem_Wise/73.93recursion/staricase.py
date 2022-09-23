def findStep(n):
	if ( n == 0 ):
		return 1
	elif (n < 0):
		return 0

	else:
		return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)


# Driver code
n =3
print(findStep(n))