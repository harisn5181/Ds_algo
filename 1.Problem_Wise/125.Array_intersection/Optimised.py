
# Bruteforce Approach TC: 0(n^2)  SC: 0(1)

from sys import stdin



#optimized Apporach   TC: 0 (n) SC: 0(1)

def intersection(arr1, arr2, n, m) :
    arr1.sort() #logn 
    arr2.sort()  #logn

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr1[i], end=' ')
            i += 1
            j += 1

# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1