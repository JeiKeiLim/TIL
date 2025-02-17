from tester import Tester
from itertools import permutations

"""
You have n tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

Constraints:
1. 1 <= tiles.length <= 7
2. tiles consists of uppercase English letters.
"""


class Solution:
    def numTilePossibilities2(self, tiles: str) -> int:
        result = set()

        queue = [("", list(tiles))]
        while queue:
            tile, tile_list = queue.pop()
            result.add(tile)
            if len(tile_list) == 0:
                continue
            for i in range(len(tile_list)):
                new_tile_list = tile_list.copy()
                new_tile = tile + new_tile_list.pop(i)
                queue.append((new_tile, new_tile_list))

        return len(result) - 1


    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        result = set()
        for i in range(n):
            for tile in permutations(tiles, i+1):
                result.add("".join(tile))

        return len(result)


if __name__ == "__main__":
    tests = [
        ["AAB"],
        ["AAABBC"],
        ["V"],
        ["ABCDEFG"]
    ]
    answers = [8, 188, 1, 13699]

    tester = Tester(Solution().numTilePossibilities2)
    tester.test(tests, answers)
