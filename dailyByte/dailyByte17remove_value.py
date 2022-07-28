# This question is asked by Google. Given a linked list and a value, 
# remove all nodes containing the provided value, and return the resulting list.

# Ex: Given the following linked lists and values...

# 1->2->3->null, value = 3, return 1->2->null
# 8->1->1->4->12->null, value = 1, return 8->4->12->null
# 7->12->2->9->null, value = 7, return 12->2->9->null

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l, v = ListNode(1, ListNode(2, ListNode(3))), 3
l1, v1 = ListNode(8, ListNode(1, ListNode(1, ListNode(4, ListNode(12))))), 1
l2, v2 = ListNode(7, ListNode(12, ListNode(2, ListNode(9)))), 7
def remove_value(l, v):
    ret = l
    while l:
        if l.next:
            while l.next.val == v:
                l.next = l.next.next
        l = l.next
    while ret.val == v:
        ret = ret.next
    while ret:
        print(ret.val)
        ret = ret.next
remove_value(l2, v2)
    # return ret