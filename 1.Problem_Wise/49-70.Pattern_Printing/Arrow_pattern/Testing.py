#18-09
"""

N=7

*
 * *
   * * *
     * * * *
   * * *
 * *
*

"""

n=11
n_half=n//2
spaces=1
i=0
star_count=2

print("*")
while (i<n_half):

    for j in range(spaces):
        print(" ",end="")

    for s in range(star_count):
        print("*",end=" ")

    spaces=spaces+2

    i=i+1

    star_count=star_count+1
    print()


spaces=spaces-4
star_count=star_count-2
for m in range(n_half-1):
    for x in range(spaces):
        print(" ",end="")

    for count in range(star_count):
        print("*",end=" ")



    star_count=star_count-1
    spaces=spaces-2
    print()
print("*",)



