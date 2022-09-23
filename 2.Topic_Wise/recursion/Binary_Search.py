def binarysearch(a,x,s,e):
  if   s>e:
    return -1
  mid=(s+e)//2
  if a[mid]==x:
    return mid
  elif a[mid] >x:
    return binarysearch(a,x,s,mid-1)
  else:
    return binarysearch(a,x,mid+1,e)


print(binarysearch([1,2,3,4,5,6,7,8,9],9,0,9))