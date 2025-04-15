from tester import Tester, generate_random_int_array
from typing import List

"""
Given an array of integers arr, and three integers a, b and c.

A triplet (arr[i], arr[j], arr[k]) is good if:
- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c

Return the number of good triplets.

Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4

Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0

Constraints:
3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
"""


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        n = len(arr)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    answer += 1
        return answer


if __name__ == "__main__":
    tests = [
        [[3, 0, 1, 1, 9, 7], 7, 2, 3],
        [[1, 1, 2, 2, 3], 0, 0, 1],
        [generate_random_int_array(100, end_n=1000), 100, 200, 300],
    ]
    answers = [4, 0, Solution().countGoodTriplets(*tests[-1])]

    tester = Tester(Solution().countGoodTriplets2)
    tester.test(tests, answers)
