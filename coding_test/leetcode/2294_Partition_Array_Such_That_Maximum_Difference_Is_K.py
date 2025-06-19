from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in each is <= 2.

Example 2:
Input: nums = [1,2,3], k = 1
Output: 2
Explanation:
We can partition into [1,2] and [3], or [1], [2,3].

Example 3:
Input: nums = [2,2,4,5], k = 0
Output: 3
Explanation:
We can partition into [2,2], [4], and [5].

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 0 <= k <= 10^5
"""


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        num = -k - 1
        answer = 0
        for n in nums:
            if n - num > k:
                num = n
                answer += 1
        return answer


if __name__ == "__main__":
    tests = [
        [[3, 6, 1, 2, 5], 2],
        [[1, 2, 3], 1],
        [[2, 2, 4, 5], 0],
        [[0], 0],
        [generate_random_int_array(10**5, end_n=10**5), 100],
    ]
    answers = [2, 2, 3, 1, -1]

    tester = Tester(Solution().partitionArray)
    tester.test(tests, answers)
