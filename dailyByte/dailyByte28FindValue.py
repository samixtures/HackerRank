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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
t = TreeNode(3, TreeNode(1), TreeNode(4))
t1 = TreeNode(7, TreeNode(5), TreeNode(9, TreeNode(8), TreeNode(10)))
t2 = TreeNode(8, TreeNode(6), TreeNode(9))
def find_value(root:TreeNode, value:int):
    if not root:
        return None
    q = [root]
    while len(q) > 0:
        if q[0].val == value:
            return q[0]
        cur_node = q.pop(0)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return None
ans = find_value(t, 1)
print(ans.val)
ans1 = find_value(t1, 9)
print(ans1.val)
ans2 = find_value(t2, 7)
print(ans2) # None type has no atrribute val