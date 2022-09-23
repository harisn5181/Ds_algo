#20-09

arr=[100,20,10,40,35]
n=5
x=38
arr.sort()


#arr=[10,20,35,40,100]


start=0
end=n-1

while start<=end:
    mid=(start+end)//2
    if arr[mid]==x:
        print("elemet found")
        break
    elif x< arr[mid]:
        end=mid-1
    elif x>arr[mid]:
        start=mid+1
else:
    print("not found")
