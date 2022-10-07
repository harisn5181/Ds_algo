
def printPairDiffK(l, k):
    d={}
    c=0
    for i in l:
        d[i]=d.get(i,0)+1


    for i in d:
        if k !=0:
            if i+k in d:
                c += d[i] * d[i + k]
        else:
            c += (d[i + k] * (d[i + k] - 1) // 2)
    return c



n=4

l=0,0,0,0
k=0
print(printPairDiffK(l, k))