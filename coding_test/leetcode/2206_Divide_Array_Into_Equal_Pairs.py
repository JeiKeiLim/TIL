from tester import Tester, generate_random_int_array
from typing import List

"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:
1. Each element belongs to exactly one pair.
2. The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.

Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation:
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

Constraints:
1. nums.length == 2 * n
2. 1 <= n <= 500
3. 1 <= nums[i] <= 500
"""


class Solution:
    def divideArray2(self, nums: List[int]) -> bool:
        num_map = [0] * 501
        for n in nums:
            num_map[n] += 1

        for val in num_map:
            if val % 2 == 1:
                return False
        return True

    def divideArray(self, nums: List[int]) -> bool:
        num_map = {}
        for n in nums:
            num_map[n] = num_map.get(n, 0) + 1

        for val in num_map.values():
            if val % 2 == 1:
                return False
        return True


if __name__ == "__main__":
    tests = [
        [[3, 2, 3, 2, 2, 2]],
        [[1, 2, 3, 4]],
        [generate_random_int_array(500000, end_n=500)],
    ]
    answers = [True, False, False]

    tester = Tester(Solution().divideArray2)
    tester.test(tests, answers)
