# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNode(head, n):
    count = 0
    # Write your code here.
    while head is not None:
        if head.data == n:
            return count
        head = head.next
        count += 1
    return -1
