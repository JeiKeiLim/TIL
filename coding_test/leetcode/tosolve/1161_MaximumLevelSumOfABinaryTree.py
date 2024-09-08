from tester import Tester  # Assuming you have a Tester class for running tests

"""
1161. Maximum Level Sum of a Binary Tree
Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

        1
       / \
      7   0
     / \
    7  -8

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

        989
          \
         10250
         /    \
      98693   -89388
                  \
                -32127

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        get_TreeNode([1, 7, 0, 7, -8, None, None]),  # Example 1
        get_TreeNode(
            [989, None, 10250, 98693, -89388, None, None, None, -32127]
        ),  # Example 2
    ]
    answers = [
        2,  # Example 1
        2,  # Example 2
    ]

    tester = Tester(Solution().maxLevelSum)
    tester.test(tests, answers)
