#Bruteforce 
# TC: 0 (n)   SC: 0 (1)


def Triangular_star_pattern(n):

  if n ==0 :
    return
  Triangular_star_pattern(n-1)
  print(str(n) * n  )

#Main
n=3
Triangular_star_pattern(n)


"""
Dry run

1
22
333
4444



"""