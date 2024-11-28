from tester import Tester

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n_island = 0
        have_landed = set()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if (x, y) in have_landed:
                    continue

                if grid[x][y] == "1":
                    island_group = [[x, y]]
                    while len(island_group) > 0:
                        cx, cy = island_group.pop(0)

                        if (cx, cy) in have_landed:
                            continue

                        have_landed.add((cx, cy))

                        if grid[cx][cy] == "0":
                            continue

                        if cx > 0:
                            island_group.append([cx-1, cy])
                        if cx < len(grid)-1:
                            island_group.append([cx+1, cy])
                        if cy > 0:
                            island_group.append([cx, cy-1])
                        if cy < len(grid[cx])-1:
                            island_group.append([cx, cy+1])

                    n_island += 1

        return n_island


if __name__ == "__main__":
    tests = [
        [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        ],
        [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        ],
    ]
    answers = [1, 3]

    tester = Tester(Solution().numIslands)
    tester.test(tests, answers)
