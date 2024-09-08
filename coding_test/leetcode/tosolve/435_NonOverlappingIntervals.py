from tester import Tester  # Assuming you have a Tester class for running tests

"""
435. Non-overlapping Intervals
Medium

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

### Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

### Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

### Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        pass  # To be implemented


if __name__ == "__main__":
    # Test cases
    tests = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]]),  # Example 1
        ([[1, 2], [1, 2], [1, 2]]),  # Example 2
        ([[1, 2], [2, 3]]),  # Example 3
    ]
    answers = [
        1,  # Expected output for Example 1
        2,  # Expected output for Example 2
        0,  # Expected output for Example 3
    ]

    tester = Tester(Solution().eraseOverlapIntervals)
    tester.test(tests, answers)
