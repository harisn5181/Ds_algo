def subset_sum(arr,output):
    length=len(arr)
    if length ==0 :

        output.append("")
        return output
    sum=subset_sum(arr[1:],output) #sum=30,"","20 30",20,
    last_digit=arr[0] # 10


    for s in sum:
            temp=str(s)
            value= str(last_digit)
            temp_1=temp+value
            output.append(temp_1) # 30,"","20 30",20,1020,1030,10, 10 20 30
    return output

arr=[10,20,30]
output=[]
subset_sum(arr,output)