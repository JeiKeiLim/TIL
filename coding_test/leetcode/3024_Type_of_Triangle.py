from tester import Tester
from typing import List

"""
You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

- A triangle is called equilateral if it has all sides of equal length.
- A triangle is called isosceles if it has exactly two sides of equal length.
- A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

Example 1:
Input: nums = [3,3,3]
Output: "equilateral"

Example 2:
Input: nums = [3,4,5]
Output: "scalene"

Constraints:
- nums.length == 3
- 1 <= nums[i] <= 100
"""


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        answer_str = ("equilateral", "isosceles", "scalene", "none")
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return answer_str[0]

        for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
            if nums[i] + nums[j] <= nums[k]:
                return answer_str[3]

        for i, j in ((0, 1), (0, 2), (1, 2)):
            if nums[i] == nums[j]:
                return answer_str[1]

        return answer_str[2]


if __name__ == "__main__":
    tests = [
        [[3, 3, 3]],
        [[3, 4, 5]],
        [[5, 5, 8]],
        [[1, 2, 3]],
        [[10, 10, 100]],
    ]
    answers = [
        "equilateral",
        "scalene",
        "isosceles",
        "none",
        "none",
    ]

    tester = Tester(Solution().triangleType)
    tester.test(tests, answers)
