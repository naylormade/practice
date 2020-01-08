# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        print(root.left)
        total = 0

        if total == sum and root.left is None and root.right is None:
            return True
        else:
            return False

        while(root):
            if total == sum:
                return True
            total += root.val
            
            root = root.left
            if root.left is None:
                root = root.right
            
        print(total)
        return False