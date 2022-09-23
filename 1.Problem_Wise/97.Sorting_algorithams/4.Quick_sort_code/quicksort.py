        #quick sort
#Base Case 
#partition
#quick sort
def partition(a,si,ei):
  pivot=a[si]
  #find number of elements smaller than pivot
  count=0
  for i in range(si,ei+1):
    if a[i]< pivot:
      count=count+1
  a[si+count],a[si]=a[si],a[si+count]    
  pivot_index=si+count

  i=si
  j=ei
  while i<j:
    if a[i] < pivot:
      i=i+1
    elif a[j] >= pivot:
      j=j-1
    else:
      a[i],a[j]=a[j],a[i]
      i=i+1
      j=j-1
  return pivot_index    

def quick_sort(a,si,ei):
  if si>=ei :
    return 
  pivot_index=partition(a,si,ei)
  quick_sort(a,si,pivot_index-1)
  quick_sort(a,pivot_index+1,ei)
 
a=[10,9,22,3,10,12,83]
quick_sort(a,0,len(a)-1)
print(a)
