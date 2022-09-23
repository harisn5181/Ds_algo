
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

# #Following is the Node class already written for the Linked List
# class Node :
#     def __init__(self, data) :
#         self.data = data
#         self.next = None



# def isPalindrome(head) :
#     #Your code goes here

































# #Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = [1,5,3]

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# #to print the linked list 
# def printLinkedList(head) :

#     while head is not None :
#         print(head.data, end = " ")
#         head = head.next

#     print()


# #main
# t = int(stdin.readline().rstrip())

# while t > 0 :
    
#     head = takeInput()
    
#     if isPalindrome(head) :
#         print('true')
#     else :
#         print('false')
        
#     t -= 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class ListNode:
   def __init__(self, data, next = None):
      self.data = data
      self.next = next
    
    
def make_list(elements):
    
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head
class Solution(object):
   def isPalindrome(self, head):
      fast,slow = head,head
      rev = None
      flag = 1
      if not head:
         return True
      while fast and fast.next:
         if not fast.next.next:
            flag = 0
            break
         fast = fast.next.next
         temp = slow
         slow = slow.next
         temp.next = rev
         rev = temp
      #print(fast.val)
      fast = slow.next
      slow.next = rev
      if flag:
         slow = slow.next
      while fast and slow:
         if fast.data != slow.data:
            return False
         fast = fast.next
         slow = slow.next
      return True
head = takeInput()
ob1 = Solution()
print(ob1.isPalindrome(head))    
    