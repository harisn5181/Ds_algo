import sys

def largest(m,n,arr):
    maxrow=0
    max_row_1=-222222
    row_index=-100

    for r in range(m):
        maxrow=0
        for c in range(n):
            maxrow=arr[r][c]+maxrow

        if maxrow >= max_row_1:
            max_row_1=maxrow
            row_index=r
    print("row",row_index,max_row_1)

    maxcolumn=0
    max_col_1=-2222
    row_index=-100

    for c in range(n):
        sum=0
        for r in range(m):
            sum=sum+arr[r][c]

        if sum>max_col_1:
            max_col_1=sum
            row_index=c
    print("column", row_index, max_col_1)





arr=[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
largest(3,3,arr)
