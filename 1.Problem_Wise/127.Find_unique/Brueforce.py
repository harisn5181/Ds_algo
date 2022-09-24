

def findUnique(arr, n):
  arr.sort()
  if n%2!=0:
      
    for i in range(0,n,2):
      if i ==(n-1):
        return arr[i]
      if arr[i] != arr[i+1]:
          return arr[i]
  else:
      return -1    


t = int(input())
while (t > 0):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(findUnique(arr, n))
    t -= 1
