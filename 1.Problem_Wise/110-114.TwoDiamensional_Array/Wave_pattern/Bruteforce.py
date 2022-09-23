from sys import stdin

def wavePrint(arr, m, n):

    Number = 3
    for i in range(n): # 5
        temp = m - 1 #3

        for j in range(m):# 4
            if Number % 2 == 0: #True
                print(arr[temp][i], end=" ")
                temp = temp - 1 #0
            else:
                print(arr[j][i], end=" ")
        Number = Number + 1

def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1