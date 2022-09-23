#Bruteforce  TC: 0 (n)   SC: 0 (1)

def inverted_number_pattern(n):
  if n==0:
    return

  print(str(n)* n)
  inverted_number_pattern(n-1)





#Main
n=int(input("Enter the number:"))
inverted_number_pattern(n)