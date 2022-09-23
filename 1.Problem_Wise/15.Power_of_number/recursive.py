"""def power(N, P):

	# if power is 0 then return 1
	# if condition is true
	# only then it will enter it,
	# otherwise not
	if P == 0: # base condition
		return 1

	# recurrence relation
	return (N*power(N, P-1))

# Driver program
N = 2
P = 3

print(power(N, P))
"""





a, b = input().split()
a = int(a)
b = int(b)

def power(a,b):
    if b==0:
        return 1

    return (a*power(a,b-1))

print(power(a,b))