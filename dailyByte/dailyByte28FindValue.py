# This question is asked by Google. Given the reference to the root of a 
# binary search tree and a search value, return the reference to the node that 
# contains the value if it exists and null otherwise.
# Note: all values in the binary search tree will be unique.

# Ex: Given the tree...

#         3
#        / \
#       1   4
# and the search value 1 return a reference to the node containing 1.
# Ex: Given the following tree...

#         7
#        / \
#       5   9
#          / \ 
#         8   10
# and the search value 9 return a reference to the node containing 9.
# Ex: Given the following tree...

#         8
#        / \
#       6   9
# and the search value 7 return null.


class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

t = TreeNode(3, TreeNode(1), TreeNode(4))

def find_node(t, v):
    print(t.val)
    if not t:
        return t
    if t.val == v:
        print("issa worked")
        return t
    if t.left:
        find_node(t.left, v)
    if t.right:
        find_node(t.right, v)

ret = find_node(t, 1)
print(ret)