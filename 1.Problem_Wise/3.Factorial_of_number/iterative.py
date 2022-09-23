#bruteforce approach
#TC:0 (n)  SC:0(1)


"""
fact= 5
n=4

fact=20
n=3

fact=60
n=2

fact=120
n=1



"""

n=5
fact=1
k=n
for i in range(k):
  fact=fact*n
  n=n-1

print(fact)
