from tester import Tester
from data_structure import TreeNode, get_TreeNode

from typing import Tuple, Optional

"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Definitions:
- A leaf node has no children.
- The depth of the root is 0; depth of children is d + 1.
- The lowest common ancestor of a set of nodes is the deepest node such that all those nodes are in its subtree.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: Leaves with values 7 and 4 are deepest. Their LCA is 2.

           3
       /        \
    5            1
  /   \\      /    \
6       2    0      8
     /    \
    7      4

Example 2:
Input: root = [1]
Output: [1]
Explanation: Root is the only node and the deepest leaf.

Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: 2 is the only deepest leaf node.

Constraints:
- The number of nodes in the tree is in [1, 1000]
- Node values are unique in range [0, 1000]
"""


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node: Optional[TreeNode], depth: int) -> Tuple[int, Optional[TreeNode]]:
            if node is None:
                return (depth, None)

            l_depth, l_lca = dfs(node.left, depth + 1)
            r_depth, r_lca = dfs(node.right, depth + 1)

            if l_depth > r_depth:
                return l_depth, l_lca

            if l_depth < r_depth:
                return r_depth, r_lca

            return l_depth, node

        return dfs(root, 0)[1]


if __name__ == "__main__":
    tests = [
        [get_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])],
        [get_TreeNode([1])],
        [get_TreeNode([0, 1, 3, None, 2])],
        [get_TreeNode([0, 1, 3, None, 2, 4, None])],
        [
            get_TreeNode(
                [
                    1,
                    2,
                    3,
                    None,
                    4,
                    6,
                    None,
                    15,
                    5,
                    10,
                    None,
                    None,
                    None,
                    None,
                    7,
                    11,
                    None,
                    8,
                    12,
                    None,
                    None,
                    None,
                    9,
                    13,
                    14,
                ]
            )
        ],
    ]
    answers = [
        get_TreeNode([2, 7, 4]),
        get_TreeNode([1]),
        get_TreeNode([2]),
        get_TreeNode([0, 1, 3, None, 2, 4, None]),
        get_TreeNode([7, 8, 12, None, 9, 13, 14]),
    ]

    tester = Tester(Solution().lcaDeepestLeaves)
    tester.test(tests, answers)
