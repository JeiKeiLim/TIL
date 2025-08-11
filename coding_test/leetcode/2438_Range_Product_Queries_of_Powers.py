from tester import Tester, generate_random_int_array

from typing import List

"""
Given a positive integer n, create a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n.
The array is sorted in non-decreasing order and uniquely determined.

You are also given a 0-indexed 2D array queries, where queries[i] = [lefti, righti].
Each query requires computing the product of all powers[j] where lefti <= j <= righti.

Return an array answers where answers[i] is the answer to the ith query modulo 10^9 + 7.

Example 1:
Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 10^9 + 7 yields the same answer, so [2,4,64] is returned.

1,2,4,8,16

2*4*8
1, 2, 8, 64, 1024

Example 2:
Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation: powers = [2]

Constraints:
- 1 <= n <= 10^9
- 1 <= queries.length <= 10^5
- 0 <= starti <= endi < powers.length
"""


class Solution:
    MOD = 10**9 + 7

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """O(n^2)"""
        powers_prev = []
        local_power = 1
        for i in range(int(n**0.5) + 1):
            powers_prev.append(local_power)
            local_power = local_power << 1

        powers = []
        power_sum = 0
        while powers_prev and power_sum < n:
            local_power = powers_prev.pop()
            if (power_sum + local_power) > n:
                continue
            power_sum += local_power
            powers.append(local_power)

        powers = powers[::-1]
        answer = []
        for li, ri in queries:
            local_sum = 1
            for i in range(li, ri + 1):
                local_sum = (local_sum * powers[i]) % self.MOD
            answer.append(local_sum)
        return answer


if __name__ == "__main__":
    tests = [
        [15, [[0, 1], [2, 2], [0, 3]]],
        [2, [[0, 0]]],
        [
            53,
            [
                [2, 3],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 0],
                [0, 3],
                [3, 3],
                [2, 3],
                [1, 1],
                [2, 3],
            ],
        ],
        [
            10**9 - 1,
            [sorted(generate_random_int_array(2, end_n=20)) for _ in range(10**5)],
        ],
    ]
    answers = [
        [2, 4, 64],
        [2],
        [512, 4, 4, 4, 1, 2048, 32, 512, 4, 512],
        Solution().productQueries(*tests[-1]),
    ]

    tester = Tester(Solution().productQueries)
    tester.test(tests, answers)
