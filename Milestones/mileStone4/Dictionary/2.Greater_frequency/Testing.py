

def maxfreq(arr):
    d={}
    for num in arr:
        if num in d:
            d[num] +=1
        else:
            d[num]=1
    
    key=0
    value =0
    
    for num in d:
        if d[num]>value:
            key=num
            value=d[num]
        
    print(key)

maxfreq( [4,1,5 ])
    
