from tester import Tester

from typing import List

"""
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
1. Only ids that appear in at least one of the two arrays should be included in the resulting array.
2. Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
   - If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.

Example 1:
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.

Example 2:
Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation:
- There are no common ids, so we just include each id with its value in the resulting list.

Constraints:
1. 1 <= nums1.length, nums2.length <= 200
2. nums1[i].length == nums2[j].length == 2
3. 1 <= idi, vali <= 1000
4. Both arrays contain unique ids.
5. Both arrays are in strictly ascending order by id.
"""


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        max_idx = 0
        num_map = {}

        for idx, num in nums1:
            num_map[idx] = num_map.get(idx, 0) + num
            max_idx = max(max_idx, idx)

        for idx, num in nums2:
            num_map[idx] = num_map.get(idx, 0) + num
            max_idx = max(max_idx, idx)

        answer = []
        for idx in range(max_idx+1):
            if idx not in num_map:
                continue
            answer.append([idx, num_map[idx]])

        return answer


if __name__ == "__main__":
    tests = [
        [[[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]],
        [[[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]],
    ]
    answers = [
        [[1, 6], [2, 3], [3, 2], [4, 6]],
        [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]],
    ]

    tester = Tester(Solution().mergeArrays)
    tester.test(tests, answers)
