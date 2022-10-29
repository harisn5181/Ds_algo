






from sys import stdin
from sys import maxsize as MAX_VALUE

def countMinStepto1(n):
    if n==1:
        return 0
    
    minSteps=[0]*(n+1)
   
    
    for currentsteps in range(2,n+1):
        
        substract1=minSteps[currentsteps-1]
        divideby2= MAX_VALUE
        divideby3= MAX_VALUE
        if currentsteps %2  ==0:
            divideby2 = minSteps[currentsteps//2]
        
        if currentsteps %3 ==0:
            divideby3=minSteps[currentsteps//3]
        
        minSteps[currentsteps]= 1+min(substract1,divideby2,divideby3)
    
    return minSteps[n]

print(countMinStepto1(100))
        
        
    