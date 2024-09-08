from tester import Tester  # Assuming you have a Tester class for running tests

"""
1448. Count Good Nodes in Binary Tree
Medium

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

        3
       / \
      1   4
     /   / \
    3   1   5

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good. Good nodes: [3, 4, 5, 3]

Example 2:

        3
       / \
      3   null
     / \
    4   2

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Good nodes: [3, 3, 4]

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        get_TreeNode([3, 1, 4, 3, None, 1, 5]),  # Example 1
        get_TreeNode([3, 3, None, 4, 2]),  # Example 2
        get_TreeNode([1]),  # Example 3
    ]
    answers = [4, 3, 1]

    tester = Tester(Solution().goodNodes)
    tester.test(tests, answers)
