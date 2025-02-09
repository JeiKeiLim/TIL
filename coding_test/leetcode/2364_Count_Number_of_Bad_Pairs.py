from tester import Tester, generate_random_int_array

from typing import List
from collections import Counter

"""
You are given a 0-indexed integer array nums.
A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

Example 1:
Input: nums = [4,1,3,3]
Output: 5
Explanation:
- The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
- The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
- The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
- The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
- The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

[4, 1, 3, 3] -> 2, 1 -> 1
[4, 1, 6, 3] -> 4, 2 -> 2

4, 1 (x)
4, 6 (o)
4, 3 (x)
1, 6 (x)
1, 3 (o)
6, 3 (x)

[4, 0, 1, 0]
[4, 0, 4, 0]

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.

1, 1, 1, 1, 1 -> 5, 1 -> 10

Constraints:
1. 1 <= nums.length <= 10^5
2. 1 <= nums[i] <= 10^9
"""


class Solution:
    def countBadPairs2(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [num - i for i, num in enumerate(nums)]
        num_map = {key: val for key, val in Counter(new_nums).items() if val > 1}
        n_good = sum([(val * (val - 1)) // 2 for val in num_map.values()])

        return ((n * (n - 1)) // 2) - n_good

    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for i in range(n - 1):
            n_bad = n - i - 1
            for j in range(i + 1, n):
                target = (j - i) + nums[i]
                if nums[j] == target:
                    n_bad -= 1
            answer += n_bad
        return answer


if __name__ == "__main__":
    tests = [
        [[4, 1, 3, 3]],
        [[4, 1, 6, 3]],
        [[1, 2, 3, 4, 5]],
        [generate_random_int_array(10**5, start_n=1, end_n=10**9)],
    ]
    answers = [5, 4, 0, -1]

    tester = Tester(Solution().countBadPairs2)
    tester.test(tests, answers)
