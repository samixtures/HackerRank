# This question is asked by Apple. 
# Given two sorted linked lists, merge them together in ascending order and return 
# a reference to the merged list

# Ex: Given the following lists...

# list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
# list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
# list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(4, ListNode(5, ListNode(6))) # return 1->2->3->4->5->6->null

def merge_linked_list(l1, l2):
    res = ListNode()
    head = res
    while l1 and l2:
        print(l2.val)
        l2 = l2.next
        if l1.val < l2.val and l1.next and l2.next:
            res.next = ListNode(l1.val)
            res = res.next
            l1 = l1.next
        # if l1.val > l2.val:
        #     res.next = ListNode(l2.val)
        #     res = res.next
        #     l2 = l2.next
    while head:
        print(head.val)
        head = head.next
merge_linked_list(l1,l2)