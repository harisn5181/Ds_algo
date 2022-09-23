

"""


Output



*
 * *
   * * *
     * * * *
   * * *
 * *
*
n=7
star_count  spaces


2              1
3              3
4              5

5-1=4







n=11


*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*



remaining=n-((n//2)+1)
remaining=11-(6)=5
remaining=7-(4)=3

"""


n=int(input())



  
spaces =0
star_count=1
#row
for i in range((n//2)+1):
  #spaces
  for s in range(spaces):
    print(" ",end="")

  for count in range(star_count):
    print("*",end=" ")
      

  spaces=spaces+2
  star_count=star_count+1
  print()
  

#reverse_row
remaining=n-((n//2)+1)
spaces=spaces-4
star_count=star_count-2

for i in range(remaining):
  #spaces

  for rev_s in range(spaces):
    print(" ",end="")

  for rev_count in range(star_count):
    print("*",end=" ")

    
      

  print()
  spaces=spaces-2
  star_count=star_count-1





