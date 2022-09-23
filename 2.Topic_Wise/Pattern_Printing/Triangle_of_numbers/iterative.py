
"""
#my brueforce approach

i = 1
k=1



def star_pattern(n):
  global i 
  while i <= n :
      spaces = 1
      while spaces <= n - i :    #is it o (n)
          print(' ', end = '')
          spaces = spaces + 1
      
      j = 0
      global k
      mid=k//2
      
      # for j in range(k):
      while (j<k):   
          if j==0:
            print (i,end=" ")
            j=j+1
          elif j<mid:
            x=i+1
        
        
            for h in range(x,k):
              print(h,end=" ")
          
            j= mid
          elif j==mid:
            j=j+1
            print(k,end=" ")
          elif j>mid:
            
            if j == k-1:
              print(i,end=" ")
              j=j+1
              break
            else:
            
            
              f=k-1
              for l in range(f,i,-1):
                
                print(l,end=" ")
              j=k-1  
          
        #put_number(n_mid,n-1,mid,temp_number_global,j)
      
          
      print()
      i = i + 1
      k=k+2

n = int(input())
star_pattern(n)    
    

"""




#another approach using for loop instead of big lines of coding


n=4
for i in range(1,n+1,1):
  for s in range(n-i):
    print(" ",end="")
  for j in range(i,2*i,1):
    print(j,end="")
  for j in range(2*i-2,i-1,-1):
    print(j,end="")

  print()

"""

Dry running this approach



   1
2 3  2 

n=4

i=1
s =n-i=4-1=3

j=1 
print(1)

j=2*i-2=0,0,
s=4-2=2
j=2,4 

j=2,1,-1=2

2


"""