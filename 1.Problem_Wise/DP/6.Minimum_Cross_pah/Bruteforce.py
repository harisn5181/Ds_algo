input_array=[[1,2,3],[4,5,6],[7,8,9]]


def minimum_crosspath(arr,i,j,m,n):

    if i >= m or j  >= n:
        return 0


    ans =arr[i][j] + min(minimum_crosspath(arr[i][j+1],i,j+1,m,n),minimum_crosspath(arr[i+1][j],i+1,j,m,n),minimum_crosspath(arr[i+1][j+1],i+1,j+1,m,n))
    return ans
m,n=3,3
print(minimum_crosspath(input_array,0,0,m,n))


