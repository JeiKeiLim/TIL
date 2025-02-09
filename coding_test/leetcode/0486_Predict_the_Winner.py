from tester import Tester

from typing import List

"""
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Rules:
1. Player 1 and player 2 take turns, with player 1 starting first.
2. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1])
   which reduces the size of the array by 1.
3. The player adds the chosen number to their score.
4. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner,
and you should also return true. You may assume that both players are playing optimally.

Example 1:
Input: nums = [1,5,2]
Output: false
Explanation:
- Player 1 can choose between 1 and 2.
- If Player 1 chooses 2, then Player 2 can choose from 1 and 5. If Player 2 chooses 5, then Player 1 will be left with 1.
- Final score: Player 1 = 3, Player 2 = 5. Hence, Player 1 cannot win.

Example 2:
Input: nums = [1,5,233,7]
Output: true
Explanation:
- Player 1 first chooses 1. Then Player 2 chooses between 5 and 7.
- No matter which number Player 2 chooses, Player 1 can then take 233.
- Final score: Player 1 = 234, Player 2 = 12. Hence, Player 1 wins.

Constraints:
1. 1 <= nums.length <= 20
2. 0 <= nums[i] <= 10^7
"""


class Solution:
    def PredictTheWinner2(self, nums: List[int]) -> bool:
        stack = [(0, 0, nums.copy())]
        while stack:
            p1, p2, scores = stack.pop()

            if len(scores) == 0:
                if p1 >= p2:
                    return True
                else:
                    continue
            new_scores = scores.copy()
            new_p1 = p1 + new_scores.pop(0)
            new_p2 = p2
            if len(new_scores) > 0:
                head_sum = sum(list(new_scores)[::2])
                tail_sum = sum(list(new_scores)[::-2])
                if head_sum > tail_sum:
                    new_p2 += new_scores.pop(0)
                else:
                    new_p2 += new_scores.pop()
            stack.append((new_p1, new_p2, new_scores))

            new_scores = scores.copy()
            new_p1 = p1 + new_scores.pop()
            new_p2 = p2
            if len(new_scores) > 0:
                head_sum = sum(list(new_scores)[::2])
                tail_sum = sum(list(new_scores)[::-2])
                if head_sum > tail_sum:
                    new_p2 += new_scores.pop(0)
                else:
                    new_p2 += new_scores.pop()
            stack.append((new_p1, new_p2, new_scores))
        return False



    def PredictTheWinner(self, nums: List[int]) -> bool:
        p12 = [0, 0]
        p_idx = 0

        while nums:
            head_sum = sum(list(nums)[::2])
            tail_sum = sum(list(nums)[::-2])

            if head_sum > tail_sum:
                p12[p_idx] += nums.pop(0)
            elif head_sum < tail_sum:
                p12[p_idx] += nums.pop()
            elif nums[0] >= nums[-1]:
                p12[p_idx] += nums.pop(0)
            else:
                p12[p_idx] += nums.pop()
            p_idx = (p_idx + 1) % 2

        print(p12)
        return p12[0] >= p12[1]


if __name__ == "__main__":
    tests = [
        [[1, 5, 2]],
        [[1, 5, 233, 7]],
        [[1, 5, 233, 2, 7]],
        [
            [
                9337301,
                0,
                2,
                2245036,
                4,
                1997658,
                5,
                2192224,
                960000,
                1261120,
                8824737,
                1,
                1161367,
                9479977,
                7,
                2356738,
                5,
                4,
                9,
            ]
        ],
    ]
    answers = [False, True, False, True]

    tester = Tester(Solution().PredictTheWinner2)
    tester.test(tests, answers)
