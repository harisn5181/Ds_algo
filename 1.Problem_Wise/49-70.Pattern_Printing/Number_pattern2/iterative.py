#Bruteforce TC :0 ()

"""

1
11
202
3003

"""

n=int(input())
print(1)
i=2
while(i<=n):
    j=1
    while(j<=i):
        if(j==1 or j==i):
            print(i-1,end='')
        else:
            print("0",end='')            
        j=j+1
    print()
    i=i+1


"""
Dry run the code 


4


1

i=2
2<=4:
  j=1
  while(1<= 2):
    if (1==1 or 1==2):
      print(1,end="")
  j=2


  2<=2:
    2==1 or 2==2
    print(1)




i=3

3<= 4:
  j=1
  while (1<=3):
    1== 1
    print(2)


  j=2
  2<=3

  2<=3

"""

