from tester import Tester

from typing import List
import random

"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
The array describes the questions of an exam, where you have to process the questions in order and decide whether to solve or skip each question.
- Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions.
- If you skip question i, you get to make the decision on the next question.

Return the maximum points you can earn for the exam.

Example 1:
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation:
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5.


Example 2:
Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation:
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7.

7, 7, 5, 5, 5


Constraints:
1. 1 <= questions.length <= 10^5
2. questions[i].length == 2
3. 1 <= pointsi, brainpoweri <= 10^5
"""


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        max_val = 0
        for i in range(n - 1, -1, -1):
            pi, bi = questions[i]
            bidx = i + bi + 1
            if bidx < n:
                dp[i] = max(dp[bidx] + pi, max_val)
            else:
                dp[i] = max(pi, max_val)
            max_val = max(max_val, dp[i])
        return max_val


if __name__ == "__main__":
    tests = [
        [[[3, 2], [4, 3], [4, 4], [2, 5]]],
        [[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]],
        [[[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]],
        [[[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(10**5)]],
    ]
    answers = [5, 7, 157, -1]
    """
    39, 123, 5, 49, 65
    """

    tester = Tester(Solution().mostPoints, verbose=0)
    tester.test(tests, answers)
