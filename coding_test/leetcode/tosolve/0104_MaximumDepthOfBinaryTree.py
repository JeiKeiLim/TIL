from tester import Tester  # Importing the Tester for testing purposes

"""
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. 

Example 1:

      3
     / \
    9  20
       /  \
      15   7

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

    1
     \
      2

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""


class Solution:
    def maxDepth(self, root) -> int:
        pass


if __name__ == "__main__":
    tests = [
        get_TreeNode([3, 9, 20, None, None, 15, 7]),  # Example 1
        get_TreeNode([1, None, 2]),  # Example 2
    ]
    answers = [3, 2]

    tester = Tester(Solution().maxDepth)
    tester.test(tests, answers)
