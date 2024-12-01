from tester import Tester

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)

        if len(nums) < 2:
            return nums[0]

        idx = (left + right) // 2
        prev_idx = idx + 1

        while prev_idx != idx:
            prev_idx = idx
            if nums[idx] == nums[idx + 1]:
                idx += 1

            if (idx-left+1) == 3:
                if nums[idx] != nums[idx-1]:
                    return nums[idx]
                else:
                    return nums[idx-2]

            if (idx-left+1) % 2 == 0:
                left = idx - 1
            else:
                right = idx + 1

            idx = (left + right) // 2

        return nums[idx + 1]


if __name__ == "__main__":
    tests = [
        [[1, 1, 2, 3, 3, 4, 4, 8, 8]],
        [[3, 3, 7, 7, 10, 11, 11]],
        [[1]],
        [[1, 2, 2, 3, 3]],
    ]
    answers = [
        2,
        10,
        1,
        1,
    ]

    tester = Tester(Solution().singleNonDuplicate)
    tester.test(tests, answers)
