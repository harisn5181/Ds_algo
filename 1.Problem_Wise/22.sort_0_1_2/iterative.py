from sys import stdin
#0       0      0      1          1        2          2
#                z                        ti

def sort012(arr, n):
    z = 0
    t = n - 1
    i = 0
    while i <= t:
        if (arr[i] == 0):
            arr[z], arr[i] = arr[i], arr[z]
            i = i + 1
            z = z + 1
        elif arr[i] == 2:
            arr[t], arr[i] = arr[i], arr[t]
            t = t - 1

        else:
            i = i + 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)

    t -= 1