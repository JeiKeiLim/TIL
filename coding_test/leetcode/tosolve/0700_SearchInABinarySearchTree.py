from tester import Tester  # Assuming you have a Tester class for running tests

"""
700. Search in a Binary Search Tree
Easy

You are given the root of a binary search tree (BST) and an integer val. 

Find the node in the BST whose value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.

Example 1:

        4
       / \
      2   7
     / \
    1   3

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

        4
       / \
      2   7
     / \
    1   3

Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 10^7
- root is a binary search tree.
- 1 <= val <= 10^7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (get_TreeNode([4, 2, 7, 1, 3]), 2),  # Example 1
        (get_TreeNode([4, 2, 7, 1, 3]), 5),  # Example 2
    ]
    answers = [
        get_TreeNode([2, 1, 3]),  # Expected subtree for val = 2
        None,  # Expected output for val = 5
    ]

    tester = Tester(Solution().searchBST)
    tester.test(tests, answers)
