# This question is asked by Facebook. Given a linked list, 
# containing unique values, reverse it, and return the result.

# Ex: Given the following linked lists...

# 1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
# 7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
# 1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l = Node(1, Node(2, Node(3)))
l1 = Node(7, Node(15, Node(9, Node(2))))
l2 = Node(1)

def reverseList(l):
    print_l = l
    prev = None
    while l:
        nxt = l.next
        l.next = prev
        prev = l
        l = nxt
    while prev:
        print(prev.val)
        prev = prev.next
reverseList(l)
reverseList(l1)
reverseList(l2)