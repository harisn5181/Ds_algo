#Bruteforce Approach 
#TC: more than 0 (n) and less than  0 (n^2  )
#SC: 0 (n)



#Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.



def checkMember(n):
  
#Implement Your Code Here
  pass

  fib0=0
  fib1=1
  fib_ser=[]
  fib_ser.append(fib0)
  fib_ser.append(fib1)
  
  while (fib1 < (n+1)):              #what is the tme complexity of                                           this loop
      fib=fib0+fib1
      fib0=fib1
      fib1=fib
      if fib<= n:
        fib_ser.append(fib)
  print(fib_ser)

  

  flag =False
  
  for i in  fib_ser:                      #0 (n) for traversing each                                                 element
    if i == n:
      flag =True


      break
  if flag==True:
    return True
  else :
    return False

        
n=int(input("enter n:  "))
if(checkMember(n)):
    print("true")
else:
    print("false")