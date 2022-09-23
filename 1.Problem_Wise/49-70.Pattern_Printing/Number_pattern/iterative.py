"""

Output

1        1
12      21
123    321
1234  4321
1234554321


Dry run


word

1 5-1 spaces 5-1 spaces 1
2 5-2 spaces 5-2 spces
3 5-3 spaces  5-3 spaces

4 5-4 spaces 5-4 spaces 4321

123455-0054321
"""

n=int(input("Enter no of rows:"))
k=1

def solution(n):
  for i in range(n):
    global k 
    
    for j in range(k):
      print(j+1,end="")
    
    for s in range(n-k):
      print(" ",end="")
  
    
    for s in range(n-k):
      print(" ",end="")
      
    
    for j in range(k,0,-1):       
      print(j,end="")  
  
    k=k+1  
    print()
  
      
solution(n)      
    




