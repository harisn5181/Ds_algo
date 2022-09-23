# this is a puzzle game question

def tower_hanoi(n,a,b,c):
  if n==1:
    print("move first disk from ",a,"to",c)
    return 
  tower_hanoi(n-1,a,c,b)
  print("move",n,"ith disk from",a,"to",c)
  tower_hanoi(n-1,b,a,c)

  

tower_hanoi(3,"a","b","c")