
def findLargest(arr, n, m):
    rmax = -2147483648
    r_index = 0
    for row in arr:
        sum = 0
        for i in row:
            sum += i
        if sum > rmax:
            rmax = sum

            r_index = arr.index(row)

    cmax = -2147483648
    c_index = 0
    for c in range(mCols):
        sum = 0
        for r in range(nRows):
            sum += arr[r][c]
        if sum > cmax:
            cmax = sum
            c_index = c

    if rmax >= cmax:
        print("row", r_index, rmax)
    else:
        print("column", c_index, cmax)


# Taking Input Using Fast I/O
def take2DInput():

    nRows = 3
    mCols = 3

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    return mat, nRows, mCols

mat, nRows, mCols = take2DInput()
findLargest(mat, nRows, mCols)

