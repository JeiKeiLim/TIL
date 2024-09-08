from tester import Tester  # Assuming you have a Tester class for running tests

"""
872. Leaf-Similar Trees
Easy

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Tree 1:

               3
           /       \
         5          1
       /   \      /   \
     6      2    9    8
           /  \
         7     4

Leaves of Tree 1: [6, 7, 4, 9, 8]


Tree 2:

               3
           /       \
         5          1
       /   \      /   \
     6     7     4     2
                     /   \
                   9      8

Leaves of Tree 2: [6, 7, 4, 9, 8]


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,9,8]
Output: true


Example 2:

Tree 1:

        1
       / \
      2   3

Leaves of Tree 1: [2, 3]


Tree 2:

        1
       / \
      3   2

Leaves of Tree 2: [3, 2]


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:
- The number of nodes in each tree will be in the range [1, 200].
- Both of the given trees will have values in the range [0, 200].
"""


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (
            get_TreeNode([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
            get_TreeNode([3, 5, 1, 6, 7, 4, 2, None, None, None, None, 9, 8]),
        ),  # Example 1
        (get_TreeNode([1, 2, 3]), get_TreeNode([1, 3, 2])),  # Example 2
    ]
    answers = [True, False]

    tester = Tester(Solution().leafSimilar)
    tester.test(tests, answers)
