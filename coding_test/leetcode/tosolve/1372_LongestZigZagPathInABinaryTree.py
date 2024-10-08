from tester import Tester  # Assuming you have a Tester class for running tests

"""
1372. Longest ZigZag Path in a Binary Tree
Medium

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follows:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.
- ZigZag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

        1
          \
            1
         /    \
       1       1
             /    \
            1      1
              \
               1
                 \
                  1

Input: root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).


Example 2:

       1
     /    \
   1       1
     \
       1
     /    \
   1       1
     \
       1

Input: root = [1,1,1,None,1,None,None,1,1,None,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).


Example 3:

Input: root = [1]
Output: 0

Constraints:
- The number of nodes in the tree is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        get_TreeNode(
            [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
        ),  # Example 1
        get_TreeNode([1, 1, 1, None, 1, None, None, 1, 1, None, 1]),  # Example 2
        get_TreeNode([1]),  # Example 3
    ]
    answers = [3, 4, 0]

    tester = Tester(Solution().longestZigZag)
    tester.test(tests, answers)
