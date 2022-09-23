"""

Dry run 

rows=4
star=3
zero=6


row star   zero   position 

1   3      6        start middle end
2   3      6        star+1  middle  end-1
3   3      6        star+1   middle  end-1
4   3      6        start+1 middle    end-1


Output

*000*000*
0*00*00*0
00*0*0*00
000***000"""

n=int(input())
start=1
end=2*n+1
mid=n+1
i=1
while i<=n:
    j=1
    while j<=2*n+1:
        if j==start or j==mid or j==end:
            print("*",end="")
        else:
                print("0",end="")
        j+=1
    start+=1
    i+=1
    end-=1
    print()
