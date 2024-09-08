from tester import Tester  # Assuming you have a Tester class for running tests

"""
437. Path Sum III
Medium

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

        10
       /  \
      5    -3
     / \     \
    3   2     11
   / \   \
  3  -2   1

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3

Explanation: The paths that sum to 8 are shown.


Example 2:

        5
       / \
      4   8
     /   / \
    11  13  4
   /  \     / \
  7    2   5   1

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (get_TreeNode([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8),  # Example 1
        (
            get_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
            22,
        ),  # Example 2
    ]
    answers = [3, 3]

    tester = Tester(Solution().pathSum)
    tester.test(tests, answers)
