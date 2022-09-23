from sys import stdin


def arrayEquilibriumIndex(arr, n):
    # Your code goes here
    total_sum = sum(arr)
    leftsum = 0
    for i in range(len(arr)):

        # total_sum is now right sum
        # for index i
        total_sum -= arr[i]

        if leftsum == total_sum:
            return i
        leftsum += arr[i]

    # If no equilibrium index found,
    # then return -1

    # return -1 if no equilibrium index is found
    return -1


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1