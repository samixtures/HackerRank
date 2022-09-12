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
        
t = TreeNode(7, TreeNode(2, TreeNode(1), TreeNode(5)), TreeNode(9))
t1 = TreeNode(8, TreeNode(3, TreeNode(2), TreeNode(6)), TreeNode(9))
t2 = TreeNode(8, TreeNode(6), TreeNode(9))

def lowest_ance(t:TreeNode, a:int, b:int):
    
    # Given a value and a tree it finds the node with that value and puts the ancestors into a list
    def findAnce(val:int, t=TreeNode):
        root = t
        if not root:
            return None
        l = []
        while root and root.val != val:
            l.append(root.val)
            if val > root.val:
                root=root.right
            elif val < root.val:
                root=root.left
        return l
    a_ance = findAnce(a, t)
    b_ance = findAnce(b, t)
    if a == t.val:
        a_ance = [t.val]
    if b == t.val:
        b_ance = [t.val]
    print("Ancestors of a and b are:")
    print(a_ance)
    print(b_ance)
    common_ance = []
    for x in a_ance:
        if x in b_ance:
            common_ance.append(x)
    return common_ance[-1]
    # This was a weird way of getting the highest common ancestor (which I did on accident) while getting iterative bfs practice
    # def bfs(root:TreeNode, common_ance:list):
    #     if not root:
    #         return
    #     q = [root]
    #     while len(q) > 0:
    #         if q[0].val in common_ance:
    #             return q[0].val
    #         cur_node = q.pop(0)
    #         if cur_node.left:
    #             q.append(cur_node.left)
    #         if cur_node.right:
    #             q.append(cur_node.right)
    # return bfs(t, common_ance)
    
print(lowest_ance(t, 1, 9))
print(lowest_ance(t1, 2, 6))
print(lowest_ance(t2, 6, 8))
