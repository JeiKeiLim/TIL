from tester import Tester

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                cnt = 1
                while n + cnt in num_set:
                    cnt += 1

                if longest < cnt:
                    longest = cnt

        return longest


if __name__ == "__main__":
    tests = [
        [[100, 4, 200, 1, 3, 2]],
        [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]],
        [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 100, 101]],
        [[0, -1]],
        [[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]],
    ]
    answers = [4, 9, 9, 2, 7]

    tester = Tester(Solution().longestConsecutive)
    tester.test(tests, answers)
