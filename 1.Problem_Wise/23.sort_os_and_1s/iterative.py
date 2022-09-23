
def sortZeroesAndOne(arr, n) :
    end=n-1
    start=0

    while (start<end):
      if arr[start] < arr[end]:
        start=start+1
      elif arr[start] == arr[end]:
        end=end-1
      elif arr[start]> arr[end] :
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
    return arr    

arr=[1, 0, 1, 1, 0, 1, 0, 1]
n=8
arrr=sortZeroesAndOne(arr,n)
print(arrr)
