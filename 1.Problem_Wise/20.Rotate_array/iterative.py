def rotatearray(N,a1,D):
    a2=[]
    
    for i in range(D):
        a2.append(a1[i])
    for i in range(N-D):
        a1[i]=a1[i+D]
    k=0
    for i in range(N-D,N):
        a1[i]=a2[k]
        k=k+1
    return a1



def takeinput():    
    N=int(input())
    a1=[]
    if N>0:
        a1=[int(x) for x in input().split()]
    D=int(input())
    return N,a1,D
t=int(input())
while t>0:
    N,a1,D=takeinput()
    li=rotatearray(N,a1,D)
    for ele in li:
        print(ele,end=" ")
    print()
    t=t-1