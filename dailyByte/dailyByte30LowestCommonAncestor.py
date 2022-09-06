# Given a binary search tree that contains unique values 
# and two nodes within the tree, a, and b, return their lowest common ancestor.
# Note: the lowest common ancestor of two nodes is 
# the deepest node within the tree such that both nodes are descendants of it.

# Ex: Given the following tree...
#        7
#       / \
#     2    9
#    / \ 
#   1   5 
# and a = 1, b = 9, return a reference to the node containing 7.
# Ex: Given the following tree...

#         8
#        / \
#       3   9
#      / \ 
#     2   6
# and a = 2, b = 6, return a reference to the node containing 3.
# Ex: Given the following tree...

#         8
#        / \
#       6   9
# and a = 6, b = 8, return a reference to the node containing 8.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def trav(h):
    if not h:
        return
    print(h.val)
    trav(h.left)
    trav(h.right)
t = TreeNode(7, TreeNode(2, TreeNode(1), TreeNode(5)), TreeNode(9))
a, b = 1, 9
trav(t)

def lowest_common_ancestor(t, a, b):
    h1 = h2 = {}
    c1 = c2 = 0
    trav(t)
    if not t:
        return t
    while t.val != a:
        trav(t.left)