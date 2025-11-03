from tester import Tester, generate_random_string, generate_random_int_array

from typing import List

"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful — no two consecutive balloons should be of the same color.

Bob can remove balloons to make the rope colorful. You are given an integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon.

Return the minimum time Bob needs to make the rope colorful.

Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: Remove balloon at index 2 (value 3). Resulting string has no consecutive duplicates.

Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: Already colorful.

Example 3:
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Remove balloons at indices 0 and 4. Time = 1 + 1 = 2.

Constraints:
• n == colors.length == neededTime.length
• 1 <= n <= 10^5
• 1 <= neededTime[i] <= 10^4
• colors contains only lowercase English letters.
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        answer = 0

        max_needed = 0
        prefix_sum = 0

        prev_color = ""
        for i in range(n):
            if prev_color == colors[i]:
                prefix_sum += neededTime[i]
                max_needed = max(max_needed, neededTime[i])
            else:
                prev_color = colors[i]
                answer += prefix_sum - max_needed
                max_needed = neededTime[i]
                prefix_sum = neededTime[i]
        answer += prefix_sum - max_needed

        return answer


if __name__ == "__main__":
    tests = [
        ["abaac", [1, 2, 3, 4, 5]],
        ["abc", [1, 2, 3]],
        ["aabaa", [1, 2, 3, 4, 1]],
        [generate_random_string(10**5), generate_random_int_array(10**5, end_n=10**4)],
    ]
    answers = [3, 0, 2, -1]

    tester = Tester(Solution().minCost)
    tester.test(tests, answers)
