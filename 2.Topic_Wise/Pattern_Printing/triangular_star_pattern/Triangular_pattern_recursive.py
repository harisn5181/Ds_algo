def square_pattern(n):
  if n==0:
    return 
  print("* "* n )
  square_pattern(n-1)  
  



#Main
n=int(input("Enter Number"))
square_pattern(n)


"""
Dry run 
5 4
4 3
3 2 
2 1 *  *
1 0 *
"""