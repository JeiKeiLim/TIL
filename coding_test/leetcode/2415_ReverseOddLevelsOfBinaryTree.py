from tester import Tester
from typing import Optional

import random

from data_structure import TreeNode, get_TreeNode

"""
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
The level of a node is the number of edges along the path between it and the root node.

Return the root of the reversed tree.

Example 1:
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation:
- The tree has only one odd level.
- The nodes at level 1 are 3, 5 respectively, which are reversed to become 5, 3.

Example 2:
Input: root = [7,13,11]
Output: [7,11,13]
Explanation:
- The nodes at level 1 are 13, 11, which are reversed to become 11, 13.

Example 3:
Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
Explanation:
- The nodes at odd levels are reversed.

Constraints:
- The number of nodes in the tree is in the range [1, 2^14].
- 0 <= Node.val <= 10^5
- root is a perfect binary tree.
"""


class Solution:
    def reverseOddLevels2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = {}

        def traverse(level: int, node: Optional[TreeNode]) -> None:
            if not node:
                return

            if level % 2 == 1:
                nodes[level] = nodes.get(level, []) + [node]

            traverse(level + 1, node.left)
            traverse(level + 1, node.right)

        traverse(0, root)
        for key in nodes.keys():
            values = [node.val for node in nodes[key]]
            for node, value in zip(nodes[key], values[::-1]):
                node.val = value
        return root

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root

        levels = [
            [root],
        ]
        stack = [(0, root)]
        while stack:  # O(n)
            level, node = stack.pop()
            while len(levels) < (level + 2):
                levels.append([])

            if node.left:
                stack.append((level + 1, node.left))
                levels[level + 1].append(node.left)

            if node.right:
                stack.append((level + 1, node.right))
                levels[level + 1].append(node.right)

        for i in range(1, len(levels), 2):
            values = [node.val for node in levels[i]]
            for node, value in zip(levels[i], values[::-1]):
                node.val = value

        return root


if __name__ == "__main__":
    tests = [
        [get_TreeNode([2, 3, 5, 8, 13, 21, 34])],
        [get_TreeNode([7, 13, 11])],
        [get_TreeNode([0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])],
        # [get_TreeNode([random.randint(0, 10**5) for _ in range(2**14 - 1)])],
    ]
    answers = [
        get_TreeNode([2, 5, 3, 8, 13, 21, 34]),
        get_TreeNode([7, 11, 13]),
        get_TreeNode([0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]),
        # get_TreeNode([random.randint(0, 10**5) for _ in range(2**14 - 1)]),
    ]

    tester = Tester(Solution().reverseOddLevels2, verbose=0)
    tester.test(tests, answers)
