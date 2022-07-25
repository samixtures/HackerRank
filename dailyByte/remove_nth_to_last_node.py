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
l = ListNode(1, ListNode(2, ListNode(3)))
n = 1 #return 1 -> 2 -> null

def remove_index(l, n):
    remove_ind = 1
    start_ind = 0
    head = l
    while l:
        if remove_ind-1 == start_ind:
            l.next = l.next.next
            start_ind += 1
        else:
            l = l.next
            start_ind += 1
    while head:
        print(head.val)
        head = head.next

def remove_nth_to_last_node(l,n):
    size = 0
    head = l
    while l:
        print(l.val)
        l = l.next
        size +=1
    remove_index = size - n
    index = 0
    ret = head
    while head:
        if remove_index-1 == index:
            pass
        else:
            head = head.next
            index += 1
    while ret:
        print(ret.val)
        ret = ret.val
    # print(remove_index)
    # print("size:", size)

# remove_nth_to_last_node(l, n)

remove_nth_to_last_node(l, n)