from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:
• Select an index i that was not selected in any previous operations.
• Add an integer in the range [-k, k] to nums[i].

Return the maximum possible frequency of any element in nums after performing the operations.

Example 1:
Input: nums = [1,4,5], k = 1, numOperations = 2
Output: 2
Explanation:
• Add 0 to nums[1] → [1,4,5]
• Add -1 to nums[2] → [1,4,4] → frequency of 4 is 2

Example 2:
Input: nums = [5,11,20,20], k = 5, numOperations = 1
Output: 2
Explanation:
• Add 0 to nums[1] → still [5,11,20,20] → frequency of 20 is 2

[1,1,10,10,10,3,4], 3, 2

[0,2,0,1,1,0,0,0,0,0,3]


Constraints:
• 1 <= nums.length <= 10^5
• 1 <= nums[i] <= 10^5
• 0 <= k <= 10^5
• 0 <= numOperations <= nums.length
"""

"""
[1,2,4,5], 2, 4

i = 1
freqs = [0,1,1,0,1,1]
sliding_sum = 2
answer = 2
"""


class Solution:
    def maxFrequencyElements(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        max_val = max(nums)

        limit = max_val + k + 1
        freqs = [0] * limit
        for n in nums:
            freqs[n] += 1

        answer = max(freqs) if freqs else 0

        sliding_sum = sum(freqs[0 : min(k + 1, limit)])
        if freqs:
            answer = max(answer, min(sliding_sum, freqs[0] + numOperations))

        for i in range(1, limit):
            if (i + k) < limit:
                sliding_sum += freqs[i + k]
            if (i - k - 1) >= 0:
                sliding_sum -= freqs[i - k - 1]

            answer = max(answer, min(sliding_sum, freqs[i] + numOperations))

        return answer

    def maxFrequencyElements2(self, nums: List[int], k: int, numOperations: int) -> int:
        max_val = max(nums)

        freqs = [0] * (max_val + k + 1)
        for n in nums:
            freqs[n] += 1

        answer = 0

        for i in range(1, len(freqs)):
            si = max(0, i - k)
            ei = min(len(freqs), i + k + 1)

            answer = max(answer, min(sum(freqs[si:ei]), freqs[i] + numOperations))

        return answer


if __name__ == "__main__":
    tests = [
        [[1, 4, 5], 1, 2],
        [[5, 11, 20, 20], 5, 1],
        [[9], 0, 0],
        [[1, 2, 4, 5], 2, 4],
        [[67, 80], 48, 1],
        [[1, 1, 1, 1, 100], 1, 1],
        [generate_random_int_array(10**5, start_n=1, end_n=10**5), 10000, 10000],
    ]
    answers = [2, 2, 1, 4, 2, 4, -1]

    tester = Tester(Solution().maxFrequencyElements)
    tester.test(tests, answers)

