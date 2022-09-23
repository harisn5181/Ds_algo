def issorted(a):
  l=len(a)
  if l==0 or l==1:
    return True
  if a[0]> a[1]:
    return False
  smallerlist=a[1:]
  issmalltersorted=issorted(smallerlist)
  return issmalltersorted

print(issorted([1,2,3,4,5,61,7]))