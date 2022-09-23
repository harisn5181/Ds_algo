
#Brtueforce: 
# TC:  0(n) for worst case,when step size = 1       SC : 0 (1)
def f_to_c(start,end,step):
  if start> end:
    return 
  
  c=(start-32)*5/9
  print(start,int(c))
  
  f_to_c(start+step,end,step)  




start=int(input())
end=int(input())
step=int(input())
f_to_c(start,end,step)  
  