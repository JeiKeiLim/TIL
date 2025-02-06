from tester import Tester, generate_random_int_array

from typing import List

"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that
a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4), (2,6,4,3), (6,2,3,4), (6,2,4,3),
(3,4,2,6), (4,3,2,6), (3,4,6,2), (4,3,6,2)

Example 2:
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples.


[1, 2, 5, 10, 25, 50]

2: (1, 2)
5: (1, 5)
10: (1, 10), (2, 5)
20: (2, 10)
25: (1, 25)
50: (1, 50), (2, 25), (5, 10)
100: (2, 50)
125: (5, 25)
250: (5, 50), (10, 25)
500: (10, 50)
1250: (25, 50)

(1, 50), (2, 25)
(1, 50), (5, 10)
(2, 25), (5, 10)

Constraints:
1. 1 <= nums.length <= 1000
2. 1 <= nums[i] <= 10^4
3. All elements in nums are distinct.
"""


class Solution:
    def tupleSameProduct2(self, nums: List[int]) -> int:
        n = len(nums)
        num_sets = {}
        for i in range(n - 1):
            x = nums[i]
            for j in range(i + 1, n):
                y = x * nums[j]
                num_sets[y] = num_sets.get(y, 0) + 1

        return sum((m * (m - 1)) for m in num_sets.values()) * 4

    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        num_sets = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                prod_num = nums[i] * nums[j]
                if prod_num not in num_sets:
                    num_sets[prod_num] = set()
                num_sets[prod_num].add((nums[i], nums[j]))

        answer = 0
        for val in num_sets.values():
            m = len(val)
            if m > 1:
                answer += (m * (m - 1)) // 2
        return answer * 8


if __name__ == "__main__":
    tests = [
        [[2, 3, 4, 6]],
        [[1, 2, 4, 5, 10]],
        [list(set(generate_random_int_array(2000, start_n=1, end_n=10**4)))],
    ]
    answers = [8, 16, Solution().tupleSameProduct(*tests[-1])]

    tester = Tester(Solution().tupleSameProduct2, verbose=0)
    tester.test(tests, answers)
