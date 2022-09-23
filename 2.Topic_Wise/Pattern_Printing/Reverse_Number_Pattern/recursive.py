"""

1
21
321
4321




This is i done before 


1
22
333
4444

n=4 Reverse_number_pattern(3)  
n=3 Reverse_number_pattern(2)  
n=2 Reverse_number_pattern(1)  
n=1 Reverse_number_pattern(0)

2 print(2,"")
1 print(1,"")
return 


3 print() 
2 print()
1  print()



return 




"""

def Reverse_second(m):
  if m == 0 :
    return 

  print(m,end="")
  Reverse_second(m-1)


 

def Reverse_number_pattern(n):
  if n ==0:
    return 
  Reverse_number_pattern(n-1)  
  print()
  Reverse_second(n)

  
  




#Main
n = int (input("enter number:"))
Reverse_number_pattern(n)
  
