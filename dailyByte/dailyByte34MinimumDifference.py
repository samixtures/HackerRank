# Given a binary search tree, return the minimum difference between any two nodes in the tree.

# Ex: Given the following tree...
#         2
#        / \
#       3   1
# return 1.
# Ex: Given the following tree...
#         29
#        /  \
#      17   50
#     /     / \
#    1    42  59
# return 8.
# Ex: Given the following tree...
#         2
#          \
#          100
# return 98.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right
t = TreeNode(2, TreeNode(3), TreeNode(1))
t1 = TreeNode(29, TreeNode(17, TreeNode(1)), TreeNode(50, TreeNode(42), TreeNode(59)))
t2 = TreeNode(2, None, TreeNode(100))
def minimum_difference(t):
    def bfs(t):
        root = t
        q = [root]
        res = [root.val]
        while len(q) > 0:
            cur_node = q.pop(0)
            if cur_node.left:
                res.append(cur_node.left.val)
                q.append(cur_node.left)
            if cur_node.right:
                res.append(cur_node.right.val)
                q.append(cur_node.right)
        return res
    print(bfs(t))

    #now lets do a 2 sum type thing with the list we got
    # loop through, subtract the first value by every other value, then store the lowest
    # of those subtracted values in a hash set or map, then do something something and wazaow
minimum_difference(t1)