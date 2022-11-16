def geoSum(n):
    if n==0:
        return 1
    s=1/2**n #1.5  +1 +0.5
    smallOutput = geoSum(n-1) #0
    return s+smallOutput




n=int(input())
print("{x:.5f}".format(x=geoSum(n)))
