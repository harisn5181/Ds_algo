







def checkNumber(arr, x):
    # Please add your code here
    

  if len(arr) == 0:
    return False
  if arr[0] == x:
    return True
  return checkNumber(arr[1:],x)

	

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

arr=[1,2,3,4,5]
x=5
print(checkNumber(arr, x))

# arr=[1]
# print(arr[1:])