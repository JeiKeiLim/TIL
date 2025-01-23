from tester import Tester, generate_random_int_array

from typing import List

"""
You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [
    [1,0],
    [1,1]
    ]

Output: 3
Explanation: All three servers can communicate with at least one other server.


Example 3:
Input: grid = [
    [1,1,0,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,1]
    ]

Output: 4
Explanation:
- The two servers in the first row can communicate with each other.
- The two servers in the third column can communicate with each other.
- The server at the bottom-right corner can't communicate with any other server.


Constraints:
1. m == grid.length
2. n == grid[i].length
3. 1 <= m <= 250
4. 1 <= n <= 250
5. grid[i][j] == 0 or 1
"""


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        connected_servers = []
        for i in range(n):
            local_connection = []
            for j in range(m):
                if grid[i][j] == 1:
                    local_connection.append((i, j))
            if len(local_connection) > 1:
                connected_servers.extend(local_connection)

        for j in range(m):
            local_connection = []
            for i in range(n):
                if grid[i][j] == 1:
                    local_connection.append((i, j))
            if len(local_connection) > 1:
                connected_servers.extend(local_connection)

        return len(set(connected_servers))


if __name__ == "__main__":
    tests = [
        [[[1, 0], [0, 1]]],
        [[[1, 0], [1, 1]]],
        [[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]],
        [[[1, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1]]],
        [[generate_random_int_array(500, end_n=1) for _ in range(500)]],
    ]
    answers = [0, 3, 4, 6, Solution().countServers(*tests[-1])]

    tester = Tester(Solution().countServers, verbose=0)
    tester.test(tests, answers)
