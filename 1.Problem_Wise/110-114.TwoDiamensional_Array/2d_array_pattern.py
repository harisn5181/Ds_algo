arr=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
m=4
n=3

k=m
for i in range(m):
    f_v=k
    while(f_v>0):
        for j in range(n):
            print(arr[i][j],end="")
        f_v=f_v-1
        print()  
    
    k=k-1   