# TC:  0(n) for worst case,when step size = 1       SC : 0 (1)

start=int(input())
end=int(input())
step=int(input())


while start<=end:
    c=(start-32)*5/9
    print(start,int(c))
    start=start+step