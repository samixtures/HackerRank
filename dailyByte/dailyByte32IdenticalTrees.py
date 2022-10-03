# Given two binary trees, return whether or not the 
# two trees are identical. Note: identical meaning they 
# exhibit the same structure and the same values at each node. Ex: Given the following trees...

#         2
#        / \
#       1   3
#     2
#    / \
#   1   3

# return true.

# Ex: Given the following trees...

#         1
#          \
#           9
#            \
#            18
#     1
#    /
#   9
#    \
#     18

# return false.

# Ex: Given the following trees...

#         2
#        / \
#       3   1
#     2
#    / \
#   1   3

# return false.   


# I think we do bfs but we add Nones and we then we check if the two lists that we added the values
# to are identical

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t1 = TreeNode(1, None, TreeNode(9, None, TreeNode(18)))
t2 = TreeNode(1, TreeNode(9, None, TreeNode(18)))
t3 = TreeNode(2, TreeNode(1), TreeNode(3))
t4 = TreeNode(2, TreeNode(1), TreeNode(3))
t5 = TreeNode(2, TreeNode(3), TreeNode(1))
t6 = TreeNode(2, TreeNode(1), TreeNode(3))

def identical_trees(t1, t2):
    def bfs(root):
        q = [root]
        res1 = [root.val]
        while len(q) > 0:
            cur_node = q.pop(0)
            if cur_node.left:
                q.append(cur_node.left)
                res1.append(cur_node.left.val)
            elif not cur_node.left:
                res1.append(None)
            if cur_node.right:
                q.append(cur_node.right)
                res1.append(cur_node.right.val)
            elif not cur_node.right:
                res1.append(None)
            # print("res1 is ", res1)
        return res1
    result1 = bfs(t1)
    result2 = bfs(t2)
    if result1 == result2:
        return True
    return False
print(identical_trees(t1, t2))
print(identical_trees(t3, t4))
print(identical_trees(t5, t6))