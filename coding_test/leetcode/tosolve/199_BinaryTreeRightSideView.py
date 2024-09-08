from tester import Tester  # Assuming you have a Tester class for running tests

"""
199. Binary Tree Right Side View
Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

        1
       / \
      2   3
       \    \
        5    4

Input: root = [1,2,3,null,5,null,4]
Output: [1, 3, 4]

Example 2:

    1
     \
      3

Input: root = [1,null,3]
Output: [1, 3]

Example 3:

Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        get_TreeNode([1, 2, 3, None, 5, None, 4]),  # Example 1
        get_TreeNode([1, None, 3]),  # Example 2
        get_TreeNode([]),  # Example 3
    ]
    answers = [
        [1, 3, 4],  # Example 1
        [1, 3],  # Example 2
        [],  # Example 3
    ]

    tester = Tester(Solution().rightSideView)
    tester.test(tests, answers)
