from tester import Tester, generate_random_2d_int_array
from typing import List
import random
import heapq

"""
You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).
These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:
• [1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.
• [2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

Example 1:
Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
Output: [3,2,3]

1: (True, [2])
2: (True, [1, 3])
3: (False, [2, 4])
4: (True, [3, 5])
5: (True, [4])

Example 2:
Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]
Output: [1,-1]

Constraints:
• 1 <= c <= 10^5
• 0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)
• connections[i].length == 2
• 1 <= ui, vi <= c
• ui != vi
• 1 <= queries.length <= 2 * 10^5
• queries[i].length == 2
• queries[i][0] is either 1 or 2.
• 1 <= queries[i][1] <= c
"""


import heapq


class Solution:
    def powerGridMaintenance2(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parent = list(range(c + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i

        for u, v in connections:
            union(u, v)

        component_heaps = {}
        for i in range(1, c + 1):
            root = find(i)
            if root not in component_heaps:
                component_heaps[root] = []
            heapq.heappush(component_heaps[root], i)

        is_online = [True] * (c + 1)
        results = []

        for op, station_id in queries:
            if op == 2:
                is_online[station_id] = False
            else:
                if is_online[station_id]:
                    results.append(station_id)
                    continue

                root = find(station_id)
                heap = component_heaps.get(root)

                while heap and not is_online[heap[0]]:
                    heapq.heappop(heap)

                if heap:
                    results.append(heap[0])
                else:
                    results.append(-1)

        return results

    def powerGridMaintenance(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """Naive."""
        power_map = {i: [True, []] for i in range(1, c + 1)}
        for i, j in connections:
            power_map[i][1].append(j)
            power_map[j][1].append(i)

        visited = set()

        def dfs(idx: int) -> int:
            if idx in visited:
                return 2**31 - 1

            visited.add(idx)
            results = []
            if power_map[idx][0]:
                results.append(idx)
            for i in power_map[idx][1]:
                result = dfs(i)
                if result < 2**31 - 1:
                    results.append(result)
            if not results:
                return 2**31 - 1
            return min(results)

        answer = []
        for op, idx in queries:
            if op == 1:
                if power_map[idx][0]:
                    answer.append(idx)
                else:
                    visited.clear()
                    result = dfs(idx)
                    if result < 2**31 - 1:
                        answer.append(result)
                    else:
                        answer.append(-1)
            else:
                power_map[idx][0] = False

        # print(power_map)
        return answer


"""
     4
     |
2(x)-3-1(x)-4(x)
"""
if __name__ == "__main__":
    n_large_test = 10**3
    tests = [
        [5, [[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]],
        [3, [], [[1, 1], [2, 1], [1, 1]]],
        [
            4,
            [[2, 3], [1, 3], [4, 1], [3, 4]],
            [
                [1, 2],
                [2, 4],
                [2, 1],
                [1, 4],
                [2, 1],
                [1, 1],
                [2, 2],
                [1, 4],
                [2, 1],
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 1],
                [1, 1],
                [2, 3],
                [2, 2],
                [2, 3],
                [1, 4],
                [2, 4],
            ],
        ],
        [
            n_large_test,
            generate_random_2d_int_array(
                n_large_test, 2, start_n=1, end_n=n_large_test
            ),
            [
                [random.randint(1, 2), random.randint(1, n_large_test)]
                for _ in range(n_large_test)
            ],
        ],
    ]
    answers = [
        [3, 2, 3],
        [1, -1],
        [2, 2, 2, 3, -1, -1],
        Solution().powerGridMaintenance(*tests[-1]),
    ]

    tester = Tester(Solution().powerGridMaintenance2)
    tester.test(tests, answers)
