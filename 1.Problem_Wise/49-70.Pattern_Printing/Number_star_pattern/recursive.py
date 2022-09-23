


def number_start_pattern(n,n_columns):
  
  if n ==0:
    return
  number_start_pattern(n-1,n_columns)
  while 



#Main
n=int(input("How many numbers of pattern you want "))

n_columns=n


number_start_pattern(n,n_columns)




"""

Dry run
n=5
n_columns=5

n=5   number_start_pattern(4,5)    *4321
n=4  number_start_pattern(3,5)     5*321
n=3 number_start_pattern(2,5)      54*21
n=2   number_start_pattern(1,5)    543*1
n=1  number_start_pattern(0,5)    5432*






return   


  5432*
#  543*1
#  54*21
#  5*321
#  *4321

"""


