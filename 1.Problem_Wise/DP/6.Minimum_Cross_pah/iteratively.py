
def mincost(cost,)



Cost=[[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
n=4
m=3
dp=[[sys.maxsize for j in range(m+1) for i in range(n+1)]]
ans=mincost(Cost,0,0,4,3,dp)
print(ans)
