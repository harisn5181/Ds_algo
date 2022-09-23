"""
#Output


   1
  12 
 123
1234

"""



n = int(input())
i = 1
while i <= n :
    spaces = 1
    while spaces <= n - i :
        print(' ', end = '')
        spaces = spaces + 1
    j = 1
    while j <= i :
        print(j, end = '')
        j = j + 1
    print()
    i = i + 1
    

"""Dry run


i=1
while 1<= 4:
    spaces=1
    while (spaces (1) <= n-i (3)):
      print('',end=")
      spaces=spaces+1

    j=1
    while(1<= 1 ):
      print(1),end=
      j=2

    print("")
    i=2


    
"""
