
def geoSum(n):
    if n==0:
        return 1
    s=1/2**n
    smallOutput = geoSum(n-1)
    return s+smallOutput




n=int(input())
print("{x:.5f}".format(x=geoSum(n)))




# print("{x:.8f}".format(x=5.222))