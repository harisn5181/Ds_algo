#  Number Star pattern 1
# Send Feedback
# Print the following pattern for given number of rows.
# Input format :

# Integer N (Total number of rows)

# Output Format :

# Pattern in N lines

# Sample Input :

#    5

# Sample Output :

#  5432*
#  543*1
#  54*21
#  5*321
#  *4321




#we cant use for loop for reversely traverse in pythhon,so we need to use while loop

# N=int(input())
# for i in range (1,N+1):
#     for j in range(N,0):
#         if i==j:
#             print("*","end")
#         else:
#             print(j,"end")








N=int(input())  
i=1  
while(i<=N):# this loop is used to print row  
    j=N
    while (j>=1):# this loop is used to print numbers in a column  
        if j!=i:  
            print(j, end='')  
        else:  
            print('*', end='')  
        j=j-1  
      
    
    i=i+1;
    print("\n" )




"""
Input= 5

Output= 
          5432*
          
          543*1
          
          54*21
          
          5*321
          
          *4321


"""