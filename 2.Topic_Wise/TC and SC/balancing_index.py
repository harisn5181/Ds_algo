
n=5
arr=[1, 4, 9, 3, 2]

prev_back_sum=0
forw_back_sum=0
Flag=False



#traversing element from o to n
for i in range(n):

  #backward part
  if i!=0:
    prev_back_sum=prev_back_sum+arr[i-1]


  #forward part
    
  if Flag == False:  
    for k in range(i+1,n):
      forw_back_sum=forw_back_sum+k
      Flag=True
  else:
    forw_back_sum=forw_back_sum-i

  #Cheching equal condition  
  if prev_back_sum==forw_back_sum:
    print(i)





#I should ask this question to them 


"""
from sys import stdin


def arrayEquilibriumIndex(arr, n) :
    prev_back_sum=0
    forw_back_sum=0
    Flag=False

    
    
    #Your code goes here
    
    for i in range(n):

  #backward part
      if i!=0:
        prev_back_sum=prev_back_sum+arr[i-1]


  #forward part
    
      if Flag == False:  
        for k in range(i+1,n):
           forw_back_sum=forw_back_sum+k
           Flag=True
      else:
        forw_back_sum=forw_back_sum-i

  #Cheching equal condition  
      if prev_back_sum==forw_back_sum:
         return i
      return -1  




























#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1
"""