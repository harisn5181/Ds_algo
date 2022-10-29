import sys

sys.setrecursionlimit(10 ** 8)


def subsetssum(copy_arr, arr, k):
    if len(arr) == 0:
        return
    subsetssum(copy_arr, arr[1:], k)

    if arr[0] == k:
        print(arr[0])

    for i in range(len(copy_arr) - len(arr)):
        if arr[0] + copy_arr[i] == k:
            print(copy_arr[i], arr[0])


# taking input
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


# main
arr, n = takeInput()
copy_arr = arr.copy()

if n != 0:
    k = int(input().strip())
    liOfLi = subsetssum(copy_arr, arr, k)



