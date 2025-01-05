from tester import Tester

from typing import List

"""
2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있습니다. 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다. 각 노드를 방문할 때마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다. 이때, 늑대는 양을 잡아먹을 기회를 노리고 있으며, 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 모든 양이 잡아먹힙니다.

각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info, 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges가 매개변수로 주어질 때, 문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리인지 return 하세요.

제한사항
- 2 ≤ info의 길이 ≤ 17
- info의 원소는 0 또는 1이며, 0은 양, 1은 늑대를 의미합니다.
- info[0]의 값은 항상 0 (루트 노드에는 항상 양이 있음)
- edges의 세로 길이 = info의 길이 - 1
- 동일한 간선에 대한 정보가 중복해서 주어지지 않음
- 항상 하나의 이진 트리 형태로 입력이 주어짐

입출력 예
info                                edges                                            result
[0,0,1,1,1,0,1,0,1,0,1,1]          [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],
                                    [4,3],[6,5],[4,6],[8,9]]                        5
[0,1,0,1,1,0,1,0,0,1,0]            [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],
                                    [4,8],[6,9],[9,10]]                            5
"""


def solution2(info: List[int], edges: List[List[int]]) -> int:
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)

    # Step 2: Initialize variables
    max_sheep = 0

    # Step 3: Define DFS function
    def dfs(node, sheep, wolves, available_nodes):
        nonlocal max_sheep

        # Update the maximum number of sheep collected
        max_sheep = max(max_sheep, sheep)

        # Check if we can continue (sheep must always outnumber wolves)
        if sheep <= wolves:
            return

        # Explore all available nodes
        for next_node in available_nodes:
            new_available_nodes = available_nodes.copy()
            new_available_nodes.remove(next_node)
            new_available_nodes.extend(
                tree[next_node]
            )  # Add children of the current node

            if info[next_node] == 0:  # If the node has a sheep
                dfs(next_node, sheep + 1, wolves, new_available_nodes)
            else:  # If the node has a wolf
                dfs(next_node, sheep, wolves + 1, new_available_nodes)

    # Step 4: Start DFS from the root node (node 0)
    dfs(0, sheep=1, wolves=0, available_nodes=tree[0])

    return max_sheep


def solution(info: List[int], edges: List[List[int]]) -> int:
    todown = [[] for _ in range(len(info))]
    for i in range(len(edges)):
        todown[edges[i][0]].append(edges[i][1])

    max_sheep = 0
    stack = [(1, 0, todown[0])]
    while stack:
        n_sheep, n_wolf, next_nodes = stack.pop()
        if n_wolf >= n_sheep:
            continue
        max_sheep = max(max_sheep, n_sheep)

        for next_node in next_nodes:
            new_nodes = next_nodes.copy()
            new_nodes.remove(next_node)
            new_nodes.extend(todown[next_node])

            if info[next_node] == 0:
                stack.append((n_sheep + 1, n_wolf, new_nodes))
            else:
                stack.append((n_sheep, n_wolf + 1, new_nodes))

    return max_sheep


if __name__ == "__main__":
    tests = [
        [
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [
                [0, 1],
                [1, 2],
                [1, 4],
                [0, 8],
                [8, 7],
                [9, 10],
                [9, 11],
                [4, 3],
                [6, 5],
                [4, 6],
                [8, 9],
            ],
        ],
        [
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [
                [0, 1],
                [0, 2],
                [1, 3],
                [1, 4],
                [2, 5],
                [2, 6],
                [3, 7],
                [4, 8],
                [6, 9],
                [9, 10],
            ],
        ],
    ]
    answers = [5, 5]

    tester = Tester(solution)
    tester.test(tests, answers)
