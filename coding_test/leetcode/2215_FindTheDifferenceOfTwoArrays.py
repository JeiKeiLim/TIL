from tester import Tester
from typing import List

"""
2215. Find the Difference of Two Arrays
Easy

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Started @ 08:30
        Ended @ 08:36

        O(nm)
        """
        answers = [[], []]

        for num in nums1:
            if num not in nums2 and num not in answers[0]:
                answers[0].append(num)

        for num in nums2:
            if num not in nums1 and num not in answers[1]:
                answers[1].append(num)

        return answers


class Solution2:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        O(n+m)
        """
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]


if __name__ == "__main__":
    tests = [
        [[1, 2, 3], [2, 4, 6]],
        [[1, 2, 3, 3], [1, 1, 2, 2]],
    ]
    answers = [[[1, 3], [4, 6]], [[3], []]]

    tester = Tester(Solution2().findDifference)
    tester.test(tests, answers)
