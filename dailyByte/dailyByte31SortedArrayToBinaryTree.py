# Given an array of numbers sorted in 
# ascending order, return a height-balanced binary search 
# tree using every number from the array.
# Note: height-balanced meaning that the level 
# of any node’s two subtrees should not differ by more than one.

# Ex: Given the following nums...

# nums = [1, 2, 3] return a reference to the following tree...
#        2
#       /  \
#      1    3
# Ex: Given the following nums...

# nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
#         3
#        / \
#       2   5
#      /   / \
#     1   4   6


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
t = [1, 2, 3]
t1 = [1, 2, 3, 4, 5, 6]

def sorted_array_to_binary_tree(l:list):
    mid = sum(l)//len(l)
    res_tree = TreeNode(l[mid])
    l.pop(mid)
    q = [res_tree]

    return l
print(sorted_array_to_binary_tree(t))