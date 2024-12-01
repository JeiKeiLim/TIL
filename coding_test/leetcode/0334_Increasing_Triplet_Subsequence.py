from tester import Tester

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that:
i < j < k and nums[i] < nums[j] < nums[k]. Otherwise, return false.

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Implement a solution that runs in O(n) time complexity and O(1) space complexity.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true

Example 2:
Input: nums = [5,4,3,2,1]
Output: false

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
"""


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min1 = (2 ** 31) - 1
        min2 = (2 ** 31) - 1

        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True

        return False


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 4, 5]],
        [[5, 4, 3, 2, 1]],
        [[2, 1, 5, 0, 4, 6]],
        [[20, 100, 10, 12, 5, 13]],
        [[1, 5, 0, 4, 1, 3]],
        [[2, 4, -2, -3]],
    ]
    answers = [
        True,
        False,
        True,
        True,
        True,
        False,
    ]

    tester = Tester(Solution().increasingTriplet)
    tester.test(tests, answers)
