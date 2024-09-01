# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        c_node = root
        
        while c_node is not None:
            right = c_node.right
            left = c_node.left
            
            if left is not None:
                while left.left is not None or left.right is not None:
                    if left.right is None:
                        left = left.left
                    else:
                        left = left.right
                
                left.right = right
                c_node.right = c_node.left
                c_node.left = None
            
            c_node = c_node.right


tests = [1,2,5,3,4,None,6]

tester = Solution()
for test in tests:
	
	tester.flatten(test)

        