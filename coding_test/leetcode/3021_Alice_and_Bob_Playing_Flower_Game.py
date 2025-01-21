from tester import Tester
import math

"""
Alice and Bob are playing a turn-based game on a circular field surrounded by flowers.

The circle represents the field, and there are x flowers in the clockwise direction between Alice and Bob, 
and y flowers in the anti-clockwise direction between them.

The game proceeds as follows:
1. Alice takes the first turn.
2. In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that side.
3. At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.

Given two integers, n and m, compute the number of possible pairs (x, y) that satisfy the conditions:
1. Alice must win the game according to the described rules.
2. The number of flowers x in the clockwise direction must be in the range [1, n].
3. The number of flowers y in the anti-clockwise direction must be in the range [1, m].

Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

Example 1:
Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

Example 2:
Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.

Constraints:
1. 1 <= n, m <= 10^5
"""


class Solution:
    def aliceBobFlowerGame(self, n: int, m: int) -> int:
        nn_even = n // 2
        nn_odd = math.ceil(n / 2)
        mn_even = m // 2
        mn_odd = math.ceil(m / 2)

        return nn_even * mn_odd + nn_odd * mn_even



if __name__ == "__main__":
    tests = [
        [3, 2],
        [1, 1],
    ]
    answers = [3, 0]

    tester = Tester(Solution().aliceBobFlowerGame)
    tester.test(tests, answers)
