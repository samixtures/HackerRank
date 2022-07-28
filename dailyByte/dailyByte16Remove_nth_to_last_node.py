# This question is asked by Facebook. 
# Given a linked list and a value n, remove the nth to last node and 
# return the resulting list.

# Ex: Given the following linked lists...

# 1->2->3->null, n = 1, return 1->2->null
# 1->2->3->null, n = 2, return 1->3->null
# 1->2->3->null, n = 3, return 2->3->null

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l, n = ListNode(1, ListNode(2, ListNode(3))), 1 # return 1 -> 2 -> null
l1, n1 = ListNode(1, ListNode(2, ListNode(3))), 2 # return 1 -> 3 -> null

# GETS SIZE OF LINKED LIST
def linked_list_size(head):
    counter = 0
    while head:
        counter += 1
        head = head.next
    return counter


def remove_nth_last_node(l, n):
    ret = l
    index = 0
    nth_last_node = linked_list_size(l) - n
    # THIS IS IF WE HAVE TO REMOVE THE FIRST NODE
    if nth_last_node == 0:
        ret = ret.next
    while l:
        if index == nth_last_node - 1:
            l.next = l.next.next
        l = l.next
        index += 1
    while ret:
        print(ret.val)
        ret = ret.next
remove_nth_last_node(l, 1)

