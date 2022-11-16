









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
            c += (d[i] * (d[i] - 1) // 2)
    return c

l=[2,2,4,4]

k=0
print(printPairDiffK(l, k))