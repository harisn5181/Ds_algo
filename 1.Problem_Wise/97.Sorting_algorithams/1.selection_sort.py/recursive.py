
def s_sort(li):
    for i in range(0,len(li),1):
        min=i
        for j in range(i+1,len(li),1):
            if(li[min]>li[j]):
                min=j
        li[i],li[min]=li[min],li[i]
    for k in range(0,len(li),1):
        print(li[k],end=" ")

t=int(input())
while(t>=1):
    n=int(input())
    li=[]
    if(n>0):
        li=[int(x) for x in input().split()]
    s_sort(li)
    print()    
    t=t-1