#a[key] will give the corresponding element,if the element is not present ,it will give list index out of range error
#But in case of a.get(key),if the element is present ,it will give the element ,if the element is not presenet,instead of throwing error,it will give None

a.get('key',0) will give 0 ,if the element is not found
a,keys()
a.values()
a.items()
for i in a:
  print(i),a[i])  #printing all the items
b={3:5,'the':4}
a.update(b)

a.pop('te')
del a[1]

a.clear()

del a #delete the dicitoanry

d={
}
for w in words:
  if w in d:
    d[w] =d[w]+1
else:
  d[w]=1

#an alternative approach for above code

d={}
for w in words:
  d[w]=d.get(w,0)+1

for w in d:
  if d[w] ==k:
    print(w)