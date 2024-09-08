from tester import Tester  # Assuming you have a Tester class for running tests

"""
450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

The deletion can be divided into two stages:
1. Search for the node to remove.
2. If the node is found, delete the node.

Example 1:

Input:

        5
       / \
      3   6
     / \    \
    2   4    7

root = [5,3,6,2,4,null,7], key = 3

Output 1:

        5
       / \
      4   6
     /      \
    2        7

Output 2:

        5
       / \
      2   6
       \    \
        4    7

Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], and another valid answer is [5,2,6,null,4,null,7].


Example 2:

Input:

        5
       / \
      3   6
     / \    \
    2   4    7

root = [5,3,6,2,4,null,7], key = 0

Output:

        5
       / \
      3   6
     / \    \
    2   4    7

Explanation: The tree does not contain a node with value = 0, so no changes are made.


Example 3:

Input:

(empty tree)

root = [], key = 0

Output:

(empty tree)

Explanation: The tree is empty, so the result remains an empty tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- Each node has a unique value.
- root is a valid binary search tree.
- -10^5 <= key <= 10^5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (get_TreeNode([5, 3, 6, 2, 4, None, 7]), 3),  # Example 1
        (get_TreeNode([5, 3, 6, 2, 4, None, 7]), 0),  # Example 2
        (get_TreeNode([]), 0),  # Example 3
    ]
    answers = [
        get_TreeNode([5, 4, 6, 2, None, None, 7]),  # Valid answer for Example 1
        get_TreeNode([5, 3, 6, 2, 4, None, 7]),  # Valid answer for Example 2
        get_TreeNode([]),  # Empty tree for Example 3
    ]

    tester = Tester(Solution().deleteNode)
    tester.test(tests, answers)
