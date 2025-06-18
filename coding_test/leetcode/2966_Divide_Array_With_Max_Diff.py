from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.
Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:
- The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. 
If there are multiple answers, return any of them.

Example 1:
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]

Example 2:
Input: nums = [2,4,2,2,5,2], k = 2
Output: []

Example 3:
Input: nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
Output: [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- n is a multiple of 3
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5

4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11
"""

from collections import Counter


class Solution:
    def divideArray4(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            answer.append(nums[i : i + 3])
        return answer

    def divideArray3(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        for a, b in zip(nums[::3], nums[2::3]):
            if b - a > k:
                return []

        return [nums[i:j] for i, j in zip(range(0, n, 3), range(3, n + 1, 3))]

    def divideArray2(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer = [[]]
        for n in nums:
            if len(answer[-1]) < 3:
                if answer[-1] and (n - answer[-1][0]) > k:
                    return []
                answer[-1].append(n)
            else:
                answer.append([n])
        return answer

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        num_map = Counter(nums)
        max_n = max(nums)
        answer = [[]]
        for i in range(1, max_n + 1):
            if i not in num_map:
                continue

            for _ in range(num_map[i]):
                if len(answer[-1]) < 3:
                    answer[-1].append(i)
                else:
                    answer.append([i])

        for i in range(len(answer)):
            if (answer[i][-1] - answer[i][0]) > k:
                return []

        return answer


if __name__ == "__main__":
    tests = [
        [[1, 3, 4, 8, 7, 9, 3, 5, 1], 2],
        [[2, 4, 2, 2, 5, 2], 2],
        [[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14],
        [generate_random_int_array((10**5) - 1, start_n=1, end_n=10**5), 1000],
    ]
    answers = [
        [[1, 1, 3], [3, 4, 5], [7, 8, 9]],
        [],
        [[2, 2, 12], [4, 8, 5], [5, 9, 7], [7, 8, 5], [5, 9, 10], [11, 12, 2]],
        [],
    ]

    tester = Tester(Solution().divideArray3, verbose=0)
    tester.test(tests, answers)
