#Bruteforce Apporach TC 0 (n^3)     SC:0 (1)
"""
Output=
   1
  2 3 2 
 3 4 5 4 3
 
 
"""

def put_number(n_mid,n,mid,temp_number_global,j):
  if n==0:
    return
  
  if j==0:
    print (n_mid,end=" ")
    j=j+1
  elif j<mid:
    i=n_mid+1
    
    
    for i in range(i,temp_number_global):
      print(i,end=" ")
      
    j= mid
  elif j==mid:
    j=j+1
    print(temp_number_global,end=" ")
  elif j>mid:
    
    if j == temp_number_global-1:
      print(n_mid,end=" ")
      j=j+1
      return 
    else:
      
      
      i=temp_number_global-1
      for i in range(i,n_mid,-1):
        
        print(i,end=" ")
      j=temp_number_global-1  
  
  put_number(n_mid,n-1,mid,temp_number_global,j)



  
def put_spaces(n):
  if n ==0:
    return 
  put_spaces(n-1)
  print(" ",end="")
  

def mirror_number_pattern(n,n_copy,j):
  global number_global 
  if n==0:
    return
  mirror_number_pattern(n-1,n_copy,j) #get all 4 rows   
  put_spaces(n_copy-n)  
  
  # put spaces for each row
  number_global=number_global+2
  temp_number_global=number_global
  
  n_mid=n
  mid=number_global//2
  put_number(n_mid,number_global,mid,temp_number_global,j)               #put numbers 
  print()                    #put spaces


#Main
n=5
n_copy=n
j=0
number_global=-1
mirror_number_pattern(n,n_copy,j)




"""
Dry run 





n=4
spaces       words
3 	   4-1			 1         
2 		4-2		 3	       
1 		4-3     5        
0 		4-4	    7

1     *

num_global=3   
3 2 1 

mid=n//2
j=0
n_mid=n

def put_number(n_mid,n,mid):
	global j
	

	if j=0  :
		print (n,end="")
	
	elif j<mid:
		i=1
		
		for i in range(i,mid):
			pirnt(i,end="")

	
	elif j==mid:
		print(n_mid)

	elif j>mid:
		i=mid+1
		for i in range(i,n_mid):
			print(i,end="")
	
	elif j = n-1:
		 print(n,end="")

	put_number(n_mid,n-1,mid)
			

   	
#first row 
number_global =1
j=0
n_mid=1
mid=0
put(1,1,0)
	global j=0
	if j==0:
		print(1)
put(1,0,0):
	

   1
  2 3 2 
 3 4 5 4 3
 


#second row
number_global=3
j=0
n_mid=2
mid= 1

put(2,3,1):
	global j =0
	if j ==0:
		print(2)

put_nummber(2,2,1):
	global j =1
	
	elif j==mid:
		print(temp_number_global)


j=2
put_nummber(2,1,1,3):
	global j =2
	
	2<1
	2==1
	2> 1
	if j ==2:
		print()
 
j=3
put_nummber(2,0,1,3):
	












#third row 
number_global=5
temp_number_global=5
j=0
n_mid=3
mid=2

put(3,n=5,2,5):
	global j =0
	
j=1
put(3,n=4,2,5):
	global=1
	1<2:
		i=4 to 5
		for 
			print(4)
	
	



j=2
put(3,n=3,2,5):
	global j = 2
2<2
2==2:


j=3
put(3,n=2,2,5):
	global j = 3
	3<2:
	3==2
3>2:
	3==
	else:
	4 and 3 
		i=4 to 3 -1
		4
	
j=4
	
put(3,n=1,2,5):
	global j=4
4<2
4==2
4>2
print()
	
"""