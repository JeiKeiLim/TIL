from tester import Tester

"""
A square triple (a, b, c) is a triple where a^2 + b^2 = c^2.

Given an integer n, return the number of square triples such that 
1 <= a, b, c <= n.

Example 1:
Input: n = 5
Output: 2
Explanation:
The square triples are (3,4,5) and (4,3,5).

Example 2:
Input: n = 10
Output: 4
Explanation:
The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

Constraints:
- 1 <= n <= 250
"""


class Solution:
    def countTriples(self, n: int) -> int:
        answer = 0
        seen = set()
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                ii = i**2
                jj = j**2
                seen.add(ii)
                seen.add(jj)
                if ii + jj in seen:
                    answer += 1
        return answer


if __name__ == "__main__":
    tests = [
        [5],
        [10],
        [12],
        [250],
    ]
    answers = [2, 4, 4, 350]

    tester = Tester(Solution().countTriples)
    tester.test(tests, answers)
