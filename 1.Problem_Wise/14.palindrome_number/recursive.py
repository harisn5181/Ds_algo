#bruteforce Apporach 

#TC :0 (n)   SC: 0 (1)

def reverse_of_number(num):
  global reverse_digt
  if num <=0 :
    return 
 
  last_digit=num%10
  reverse_digt=(reverse_digt*10 )+last_digit
  reverse_of_number(num//10)
  return reverse_digt




reverse_digt=0
num=int(input("enter number"))


if num == reverse_of_number(num):
  print("its a palindrome")
else:
  print("not a palindrome ")




"""Dry Run

n=121
reverse_of_number(15) 153    3
reverse_of_number(1)   15 5  
reverse_of_number(0)   1   1     
return 



reverse_digt=(reverse_digit*10 )+digit   reverse_digit= 0 + 3 =3
reverse_digt=(reverse_digit*10 )+digit    (30) +5  =35
reverse_digt=(reverse_digit*10 )+digit     351


"""