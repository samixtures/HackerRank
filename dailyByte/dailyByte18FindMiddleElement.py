# This question is asked by Amazon. Given a non-empty linked list, 
# return the middle node of the list. If the linked list contains an even number of elements, 
# return the node closer to the end.
# Ex: Given the following linked lists...

# 1->2->3->null, return 2
# 1->2->3->4->null, return 3
# 1->null, return 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l = ListNode(1, ListNode(2, ListNode(3))) # return 2
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4)))) # return 3
l2 = ListNode(1) # return 1

# GETS SIZE OF LINKED LIST
def linked_list_size(l):
    counter = 0
    while l:
        counter+=1
        l = l.next
    return counter

def find_middle_element(l):
    index = 0
    #THIS SIZE THING IS VERY IMPORTANT, DON'T DO "linkd_list_size(l) INSIDE THE WHILE LOOP. THE LINKED LIST CHANGES SIZE I GUES..."
    size = linked_list_size(l)
    # CHECK IF IT'S AN ODD NUMBER
    if size % 2 == 1:
        while l:
            if index ==  (size // 2):
                print(l.val)
            index += 1
            l = l.next
    # CHECK IF IT'S AN EVEN NUMBER
    elif size % 2 == 0:
        while l:
            if index ==  (size // 2):
                print(l.val)
            index += 1
            l = l.next

find_middle_element(l2)