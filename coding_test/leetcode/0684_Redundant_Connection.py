from tester import Tester, generate_random_int_array

from typing import List

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
1. n == edges.length
2. 3 <= n <= 1000
3. edges[i].length == 2
4. 1 <= ai < bi <= edges.length
5. ai != bi
6. There are no repeated edges.
7. The given graph is connected.

1 - 3 - 4
| / |
5   2
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        edge_map = [[] for _ in range(n + 1)]
        answer_edge = [-1, -1]
        for node_from, node_to in edges:
            edge_map[node_to].append(node_from)
            edge_map[node_from].append(node_to)

            queue = [node_from]
            visited = set()
            while queue and answer_edge == [-1, -1]:
                node = queue.pop()

                if node in visited:
                    answer_edge = [node_from, node_to]
                    continue

                visited.add(node)
                for next_node in edge_map[node]:
                    if next_node != node and next_node not in visited:
                        queue.append(next_node)

        return answer_edge


if __name__ == "__main__":
    tests = [
        [[[1, 2], [1, 3], [2, 3]]],
        [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]],
        [[[1, 3], [3, 4], [1, 5], [3, 5], [2, 3]]],
        # [[generate_random_int_array(2, start_n=1, end_n=1000) for _ in range(1000)]]
    ]
    answers = [[2, 3], [1, 4], [3, 5], [-1, -1]]

    tester = Tester(Solution().findRedundantConnection)
    tester.test(tests, answers)
