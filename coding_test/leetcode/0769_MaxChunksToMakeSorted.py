from tester import Tester

from typing import List

"""
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk.
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
- Splitting into two or more chunks will not return the required result.
- For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]

Output: 4
Explanation:
- We can split into two chunks, such as [1, 0], [2, 3, 4].
- However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

[4, 3, 1, 0, 2]

[2, 0, 1, 3, 4]

[2, 0, 1],

Constraints:
n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        j = 0
        result = 0
        for i in range(1, len(arr)+1):
            if sorted_arr[j:i] == sorted(arr[j:i]):
                j = i
                result += 1
        return result


if __name__ == "__main__":
    tests = [
        [[4, 3, 2, 1, 0]],
        [[1, 0, 2, 3, 4]],
        [[2, 1, 0, 4, 3]],
    ]
    answers = [
        1,
        4,
        2,
    ]

    tester = Tester(Solution().maxChunksToSorted)
    tester.test(tests, answers)
