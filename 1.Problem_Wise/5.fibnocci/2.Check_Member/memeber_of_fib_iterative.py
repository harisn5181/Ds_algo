#Bruteforce Approach 
#TC: more than 0 (n) and less than  0 (n^2  )
#SC: 0 (n)



#Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.



def checkMember(n):
  
#Implement Your Code Here
  

  fib0=0
  fib1=1

  while (fib1 < (n+1)):              #what is the tme complexity of                                           this loop
      fib=fib0+fib1
      fib0=fib1
      fib1=fib
      if fib<= n: 
        if fib==n:
          print("yes")
    


  


n=int(input("enter n:  "))
checkMember(n)