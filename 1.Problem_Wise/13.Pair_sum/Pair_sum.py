def pairsum(arr,n,num):
    arr=sorted(arr)
    count=0
    numpair=0
    startindex=0
    endindex=n-1

    while (startindex<endindex):
        tempsum=arr[startindex]+arr[endindex]
        if tempsum<num:
            startindex+=1
        elif tempsum >num:
            endindex-=1
        else:
            if (arr[startindex]==arr[endindex]):
                numele=endindex-startindex
                numpair+= (numele*(numele+1))//2
                return numpair

            elementatstart=arr[startindex]
            elementatend=arr[endindex]

            tempstartindex=startindex+1
            tempendindex=endindex-1

            while tempstartindex<= tempendindex and arr[tem]


    return count

arr=[1,2,3,4,5,6]
print(pairsum(arr,6,5))