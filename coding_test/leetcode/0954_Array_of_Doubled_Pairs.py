from tester import Tester, generate_random_int_array

from typing import List

"""
Given an integer array of even length arr, return true if it is possible to reorder arr such that
arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:
Input: arr = [3,1,3,6]
Output: false

Example 2:
Input: arr = [2,1,2,6]
Output: false

Example 3:
Input: arr = [4,-2,2,-4]
Output: true
Explanation:
We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Constraints:
1. 2 <= arr.length <= 3 * 10^4
2. arr.length is even.
3. -10^5 <= arr[i] <= 10^5
"""


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n = len(arr)
        arr_map = {}
        for num in arr:
            arr_map[num] = arr_map.get(num, 0) + 1

        arr.sort()
        n_possible = 0
        for i in range(n):
            key = arr[i] * 2
            if key not in arr_map or arr[i] not in arr_map:
                continue
            if arr[i] == 0 and arr_map[key] % 2 != 0:
                continue
            if arr_map[key] > 0 and arr_map[arr[i]] > 0:
                n_possible += 1
                arr_map[key] -= 1
                arr_map[arr[i]] -= 1

        return n_possible == (n // 2)


if __name__ == "__main__":
    tests = [
        [[3, 1, 3, 6]],
        [[2, 1, 2, 6]],
        [[4, -2, 2, -4]],
        [[2, 4, 0, -1]],
        [[2, 4, 0, 0, 8, 1]],
        [[1, 2, 1, -8, 8, -4, 4, -4, 2, -2]],
        [generate_random_int_array(3 * 10**5, start_n=-(10**5), end_n=10**5)],
    ]
    answers = [
        False,
        False,
        True,
        False,
        True,
        True,
        False,
    ]

    tester = Tester(Solution().canReorderDoubled, verbose=0)
    tester.test(tests, answers)
