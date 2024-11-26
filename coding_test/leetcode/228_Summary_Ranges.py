from tester import Tester
from typing import List

"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Constraints:
0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Started @ 11:26
        Ended @ 11:39
        """
        if len(nums) < 1:
            return []

        a = nums[0]
        b = a

        num_list = [[a]]
        for i in range(1, len(nums)):
            n = nums[i]

            if n - b > 1:
                num_list.append([])

            num_list[-1].append(n)
            b = n

        result = []
        for num in num_list:
            result.append(f"{num[0]}")
            if len(num) > 1:
                result[-1] += f"->{num[-1]}"

        return result


if __name__ == "__main__":
    tests = [
        [[0, 1, 2, 4, 5, 7]],
        [[0, 2, 3, 4, 6, 8, 9]],
    ]
    answers = [["0->2", "4->5", "7"], ["0", "2->4", "6", "8->9"]]

    tester = Tester(Solution().summaryRanges)
    tester.test(tests, answers)
