"""
*000*000*
0*00*00*0
00*0*0*00
000***000"""
n=4
start=1
mid=n+1
end=2*n+1

for i in range(1,n+1):
    j=1
    while j <= 2*n+1:
        if j ==start or j==mid or j==end:
            print("*",end="")
        else:
            print("0",end="")
        j=j+1
    start=start+1
    end=end-1
    print()