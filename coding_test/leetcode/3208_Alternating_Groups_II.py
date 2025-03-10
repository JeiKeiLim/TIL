from tester import Tester, generate_random_int_array

from typing import List

"""
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. 

The color of tile i is represented by colors[i]:
1. colors[i] == 0 means that tile i is red.
2. colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating colors 
(each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Example 1:
Input: colors = [0,1,0,1,0], k = 3
Output: 3

[0,1,0,1,0,0,1]

[0,1,0]
[1,0,1]
[0,1,0]
[1,0,0]
[0,0,1]

Example 2:
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2

[0,1,0,0,1,0,1, 0,1,0,0,1]
[0,1,0,0]
[0,1,0,1,0,1]
[1,0,1,0,1,0]

Example 3:
Input: colors = [1,1,0,1], k = 4
Output: 0

Constraints:
1. 3 <= colors.length <= 10^5
2. 0 <= colors[i] <= 1
3. 3 <= k <= colors.length
"""


class Solution:
    def alternatingGroups3(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        n = len(colors)
        n_alter = 1
        answer = 0
        for i in range(1, n):
            if colors[i-1] != colors[i]:
                n_alter += 1
            else:
                if n_alter >= k:
                    answer += n_alter - k + 1
                n_alter = 1

        if n_alter >= k:
            answer += n_alter - k + 1
        return answer


    def alternatingGroups2(self, colors: List[int], k: int) -> int:
        n = len(colors)
        n_alter = 1
        current = colors[0]
        answer = 0
        for i in range(1, n + k - 1):
            next_color = colors[i % n]
            if current != next_color:
                n_alter += 1
            else:
                if n_alter >= k:
                    answer += n_alter - k + 1
                n_alter = 1

            current = next_color

        if n_alter >= k:
            answer += n_alter - k + 1

        return answer

    def alternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        n_alter = 1
        current = colors[0]
        answer = 0
        for i in range(1, n + k - 1):
            idx = i % n
            if current != colors[idx]:
                n_alter += 1
            else:
                n_alter = 1

            current = colors[idx]
            if n_alter == k:
                answer += 1
                n_alter -= 1

        return answer


if __name__ == "__main__":
    tests = [
        [[0, 1, 0, 1, 0], 3],
        [[0, 1, 0, 0, 1, 0, 1], 6],
        [[1, 1, 0, 1], 4],
        [[0, 1, 1], 3],
        [generate_random_int_array(10**6, end_n=1), 10],
    ]
    answers = [3, 2, 0, 1, Solution().alternatingGroups(*tests[-1])]


    tester = Tester(Solution().alternatingGroups3)
    tester.test(tests, answers)
