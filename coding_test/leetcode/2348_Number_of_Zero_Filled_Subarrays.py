from tester import Tester, generate_random_int_array

from typing import List

"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
- [0] occurs 4 times
- [0,0] occurs 2 times
Total = 6

Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
- [0] occurs 5 times
- [0,0] occurs 3 times
- [0,0,0] occurs 1 time
Total = 9

Example 3:
Input: nums = [2,10,2019]
Output: 0

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def zeroFilledSubarray3(self, nums: List[int]) -> int:
        answer = 0
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
                answer += zero_cnt
            else:
                zero_cnt = 0

        return answer

    def zeroFilledSubarray2(self, nums: List[int]) -> int:
        answer = 0
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
                continue
            answer += (zero_cnt * (zero_cnt + 1)) // 2
            zero_cnt = 0

        answer += (zero_cnt * (zero_cnt + 1)) // 2
        return answer

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """Naive"""
        zero_map = {}
        zero_cnt = -1
        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                zero_cnt = -1

            for i in range(zero_cnt + 1):
                if i not in zero_map:
                    zero_map[i] = 1
                else:
                    zero_map[i] += 1
        return sum(zero_map.values())


if __name__ == "__main__":
    tests = [
        [[1, 3, 0, 0, 2, 0, 0, 4]],
        [[0, 0, 0, 2, 0, 0]],
        [[2, 10, 2019]],
        [generate_random_int_array(10**5, start_n=0, end_n=0)],
    ]
    answers = [6, 9, 0, -1]

    tester = Tester(Solution().zeroFilledSubarray3)
    tester.test(tests, answers)
