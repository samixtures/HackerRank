# Given a binary search tree, rearrange the tree such that it forms a linked 
# list where all its values are in ascending order.

# Ex: Given the following tree...
#         5
#        / \
#       1   6
# return...

# 1
#  \
#   5
#    \
#     6
# Ex: Given the following tree...

#        5
#       / \
#     2    9
#    / \ 
#   1   3 
# return...

# 1
#  \
#   2
#    \
#     3
#      \
#       5
#        \
#         9
# Ex: Given the following tree...

# 5
#  \
#   6
# return...

# 5
#  \
#   6

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t = TreeNode(5, TreeNode(1), TreeNode(6))
l = []

def traverse(t, l): # tree and list (add stuff to the list)
    if not t:
        return
    if t.left:
        traverse(t.left, l)
    print(t.val)
    l.append(t.val)
    if t.right:
        traverse(t.right, l)

traverse(t, l)
print("l is ", l)




new_t = TreeNode(l[0])
new_t_ref = new_t
l.pop(0)
while l:
    new_t.right = TreeNode(l[0])
    new_t = new_t.right
    print("l is ", l)
    l.pop(0)



def prin(t):
    if not t:
        return
    print(t.val)
    if t.right:
        prin(t.right)
print("PRINTING NEW_T")
prin(new_t_ref)
