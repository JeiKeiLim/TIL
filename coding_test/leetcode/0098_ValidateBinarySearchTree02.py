# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
        if root is None:
            return True
        
        val = root.val
        
        if val <= lower or val >= upper:
            return False
        
        left = self.isValidBST(root.left, lower=lower, upper=val)
        right = self.isValidBST(root.right, lower=val, upper=upper)
        
        if not left or not right:
            return False
        else:
            return True