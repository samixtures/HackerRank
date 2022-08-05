# This question is asked by Apple. Given a potentially cyclical linked list where each value is unique, 
# return the node at which the cycle starts. If the list does not contain a cycle, return null.

# Ex: Given the following linked lists...

# 1->2->3, return null
# 1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
# 1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def print_nodes(l):
    h = l
    while h:
        print(h.val)
        h = h.next
l = ListNode(1, ListNode(2, ListNode(3)))
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l2 = ListNode(1, ListNode(9, ListNode(3, ListNode(7))))
# 1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

#l1_ref_ref is a reference to the head of a cyclical linked list
l1_ref = l1
l1_ref_ref = l1_ref
while l1_ref.next:
    print(l1_ref.val)
    l1_ref = l1_ref.next
l1_ref.next = l1.next

#l2_ref_ref is a reference to the head of a cyclical linked list
l2_ref = l2
l2_ref_ref = l2_ref
while l2_ref.next:
    print(l2_ref.val)
    l2_ref = l2_ref.next
l2_ref.next = l2.next
