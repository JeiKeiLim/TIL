from tester import Tester

from typing import List, Optional

"""
라이언은 이진트리를 구성하는 특별한 규칙을 만들어 게임을 준비했습니다. 주어진 좌표들을 이용해 이진트리를 만들고, 전위 순회(preorder)와 후위 순회(postorder)를 한 결과를 반환하세요.

제한사항
- nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열입니다.
- nodeinfo의 길이는 1 이상 10,000 이하입니다.
- nodeinfo[i]는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있습니다.
- 모든 노드의 좌표 값은 0 이상 100,000 이하인 정수입니다.
- 트리의 깊이가 1,000 이하인 경우만 입력으로 주어집니다.
- 모든 노드의 좌표는 문제에 주어진 규칙을 따릅니다.

입출력 예
nodeinfo	result
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
"""


class TreeNode:
    def __init__(
        self,
        val: int,
        x: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.x = x
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, x={self.x}, left={self.left}, right={self.right})"

    def insert(self, node: "TreeNode") -> None:
        cur = self
        while True:
            if node.x < cur.x:
                if cur.left is None:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    break
                cur = cur.right


def solution(nodeinfo: List[List[int]]) -> List[List[int]]:
    nodes = sorted(enumerate(nodeinfo, start=1), key=lambda x: (-x[1][1], x[1][0]))
    root = TreeNode(nodes[0][0], nodes[0][1][0])
    for i in range(1, len(nodes)):
        node = TreeNode(nodes[i][0], nodes[i][1][0])
        root.insert(node)

    pre_result = []
    post_result = []
    stack: List[Optional[TreeNode]] = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue

        pre_result.append(node.val)
        stack.append(node.right)
        stack.append(node.left)

    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue

        stack.append(node.left)
        post_result.append(node.val)
        stack.append(node.right)

    post_result = post_result[::-1]

    return [pre_result, post_result]


if __name__ == "__main__":
    tests = [
        [[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]],
    ]
    answers = [
        [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
