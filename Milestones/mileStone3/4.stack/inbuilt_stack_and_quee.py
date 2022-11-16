import queue


#for stack we can use list and implement ,but we cant do anything  for quee,so we use inbuilt library




#inbuilt queue function



# q=queue.Queue()

# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)

# while not q.empty():
#   print(q.get())








#lifo quee stack

q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
  print(q.get())



