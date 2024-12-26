from tester import Tester
from typing import Optional, List

from data_structure import TreeNode, get_TreeNode

"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        results = [root.val]

        next_stack = [root.left, root.right]
        while next_stack:
            stack = next_stack
            if not stack:
                continue

            next_stack = []
            max_val = -(2 ** 31)
            while stack:
                node = stack.pop()
                if not node:
                    continue
                max_val = max(max_val, node.val)
                next_stack += [node.left, node.right]

            results.append(max_val)

        results.pop()
        return results


if __name__ == "__main__":
    tests = [
        [get_TreeNode([1, 3, 2, 5, 3, None, 9])],  # Tree representation as a list
        [get_TreeNode([1, 2, 3])],
    ]
    answers = [
        [1, 3, 9],
        [1, 3],
    ]

    tester = Tester(Solution().largestValues)
    tester.test(tests, answers)
