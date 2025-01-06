from tester import Tester

from typing import List

"""
You are given an integer array nums of length n.
Your goal is to start at index 0 and reach index n - 1.
You can only jump to indices greater than your current index.
The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.

Example 1:
Input: nums = [1,3,1,5]
Output: 7
Explanation:
- First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:
Input: nums = [4,3,1,3,2]
Output: 16
Explanation:
- Jump directly to the last index. The final score is 4 * 4 = 16.

Constraints:
1. 1 <= nums.length <= 10^5
2. 1 <= nums[i] <= 10^5
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        i = 0
        j = 0
        max_val = nums[i]
        answer = 0
        for j in range(1, len(nums)):
            if nums[j] > max_val:
                answer += (j-i) * max_val
                i = j
                max_val = nums[j]
        answer += (j-i) * max_val

        return answer


if __name__ == "__main__":
    tests = [
        [[1, 3, 1, 5]],
        [[4, 3, 1, 3, 2]],
    ]
    answers = [7, 16]

    tester = Tester(Solution().maxScore)
    tester.test(tests, answers)
