# Given a binary tree, return its level 
# order traversal where the nodes in each level 
# are ordered from left to right.

# Ex: Given the following tree...

#     4
#    / \
#   2   7
# return [[4], [2, 7]]
# Ex: Given the following tree...

#     2
#    / \
#   10  15
#         \
#          20
# return [[2], [10, 15], [20]]
# Ex: Given the following tree...

#     1
#    / \
#   9   32
#  /      \
# 3        78
# return [[1], [9, 32], [3, 78]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
t = TreeNode(4, TreeNode(2), TreeNode(7))
t1 = TreeNode(2, TreeNode(10), TreeNode(15, None, TreeNode(20)))
t2=TreeNode(1, TreeNode(9, TreeNode(3)), TreeNode(32, None, TreeNode(78)))

def gather_levels(root:TreeNode):
    q = [root]
    res = [root.val]
    while len(q) > 0:
        temp = []
        for i in range(len(q)):
            cur_node = q.pop(0)
            if cur_node.left:
                temp.append(cur_node.left.val)
                q.append(cur_node.left)
            if cur_node.right:
                temp.append(cur_node.right.val)
                q.append(cur_node.right)
        res.append(temp)
    res.pop(-1)
    return res

print(gather_levels(t))
print(gather_levels(t1))
print(gather_levels(t2))

