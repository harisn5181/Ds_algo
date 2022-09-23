def reverse(l):
  lenth=len(l)

  for i in range(lenth//2):
    l[i],l[lenth-i-1]= l[lenth-i-1], l[i]


l=[1,2,3,4,5]
reverse(l)
print(l)  