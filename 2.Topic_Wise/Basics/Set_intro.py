# #set are same like list ,bt the difference is ,its used { brackets}
# function works:
# in ,for ,len,a.add('temp'),  a.update(b) it will only update if the value is not presenet in therer  ,a.remove("temp") ,a.discard(r') discard will not give error when elemenet is not presenet  ,  a.pop() it will remove any element from tuple
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
#                                                                            union and disjoint  only avaiable in sets

#sets union
a={1,2,3,4}
b={3,4,5,6}
#print(a.intersection(b))
#print(a.union(b))

#difference 
print(a.difference(b))
#print(a.symmetric_difference(b))

print(a.intersection_update(b))

a.issubset(b)
a.issuperset(b)
a.isdisjoint(s)


s=set() will create empty set