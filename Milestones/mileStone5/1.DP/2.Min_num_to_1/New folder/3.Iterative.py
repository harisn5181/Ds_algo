








from sys import stdin
from sys import maxsize as MAX_VALUE

def CountMinimum_DP(n, arr):
    for i in range(4,n+1):
        first = 1 + arr[i-1]
        second = MAX_VALUE
        third = MAX_VALUE
        if(i % 2 == 0):
            second = 1 + arr[i//2]
        if(i % 3 == 0):
            third = 1 + arr[i//3]    
        arr.append(min(first, second, third))
    return arr[n]


def countMinStepsToOne(n) :
    arr = []
    arr.append(0)
    arr.append(0)
    arr.append(1)
    arr.append(1)
    return CountMinimum_DP(n, arr)



#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))