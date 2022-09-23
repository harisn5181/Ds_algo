
# Bruteforce Approach TC: 0(n^2)  SC: 0(1)

from sys import stdin


def intersection(arr1, arr2, n, m) :
 	#Your code goes here
     for i in range(n):
         for j in range(m):
             if arr1[i] ==arr2[j]:
                 print(arr1[i],end="")
                 arr2[j]=-22222222222
                 break


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