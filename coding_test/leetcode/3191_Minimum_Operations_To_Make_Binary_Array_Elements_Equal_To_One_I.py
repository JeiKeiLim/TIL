from tester import Tester, generate_random_int_array
from typing import List

"""
You are given a binary array nums.
You can do the following operation on the array any number of times (possibly zero):
- Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1.
If it is impossible, return -1.

Example 1:
Input: nums = [0,1,1,1,0,0]
Output: 3
Explanation:
- Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
- Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
- Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

Example 2:
Input: nums = [0,1,1,1]
Output: -1
Explanation:
- It is impossible to make all elements equal to 1.

Example 3:
Input nums = [1,0,1,1,0,0,1,0,0,1,0]

1,0,1,1,0,0,1,0,0,1,0

answer: 5
1,1,0,0,0,0,1,0,0,1,0
1,1,1,1,1,0,1,0,0,1,0
1,1,1,1,1,0,1,1,1,0,0
1,1,1,1,1,0,1,1,0,1,1
1,1,1,1,1,1,0,0,0,1,1
1,1,1,1,1,1,1,1,1,1,1


1,0,0,1,1,0,1,1,1,0,0,0,1,0,1

1,1,1,0,1,0,1,1,1,0,0,0,1,0,1
1,1,1,1,0,1,1,1,1,0,0,0,1,0,1
1,1,1,1,1,0,0,1,1,0,0,0,1,0,1
1,1,1,1,1,1,1,0,1,0,0,0,1,0,1
1,1,1,1,1,1,1,1,0,1,0,0,1,0,1
1,1,1,1,1,1,1,1,1,0,1,0,1,0,1
1,1,1,1,1,1,1,1,1,1,0,1,1,0,1
1,1,1,1,1,1,1,1,1,1,1,0,0,0,1
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

Constraints:
1. 3 <= nums.length <= 10^5
2. 0 <= nums[i] <= 1
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        total = sum(nums)
        for i in range(n):
            if nums[i] == 1:
                continue

            ei = min(i + 3, n)
            si = ei - 3
            for j in range(si, ei):
                if nums[j] == 0:
                    nums[j] = 1
                    total += 1
                else:
                    nums[j] = 0
                    total -= 1
            answer += 1

            if total == n:
                return answer

        return -1


if __name__ == "__main__":
    tests = [
        [[0, 1, 1, 1, 0, 0]],
        [[0, 1, 1, 1]],
        [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]],
        [[1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]],
        [generate_random_int_array(10**5, end_n=1)],
    ]
    answers = [3, -1, 6, 9, -1]

    tester = Tester(Solution().minOperations)
    tester.test(tests, answers)
