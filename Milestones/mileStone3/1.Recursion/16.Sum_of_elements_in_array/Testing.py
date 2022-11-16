










arr=[1,2,3]

def sum(arr):
    if len(arr)==0:
        return 0

    s_sum=sum(arr[1:])
    s_sum=s_sum+arr[0]
    return s_sum

print(sum(arr))