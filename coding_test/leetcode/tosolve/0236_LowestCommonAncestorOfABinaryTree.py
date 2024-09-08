from tester import Tester  # Assuming you have a Tester class for running tests

"""
236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

    1
   /
  2

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (
            get_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            get_TreeNode([5]),
            get_TreeNode([1]),
        ),  # Example 1
        (
            get_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            get_TreeNode([5]),
            get_TreeNode([4]),
        ),  # Example 2
        (get_TreeNode([1, 2]), get_TreeNode([1]), get_TreeNode([2])),  # Example 3
    ]
    answers = [get_TreeNode([3]), get_TreeNode([5]), get_TreeNode([1])]

    tester = Tester(Solution().lowestCommonAncestor)
    tester.test(tests, answers)
