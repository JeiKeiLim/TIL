from tester import Tester

"""
On day 1, one person discovers a secret.

You are given:
- An integer `delay`, meaning each person shares the secret with a new person every day starting from `delay` days after discovering the secret.
- An integer `forget`, meaning each person forgets the secret `forget` days after discovering it. They cannot share it on the day they forget or afterwards.

Given an integer `n`, return the number of people who know the secret at the end of day `n`.

Return the result modulo 10^9 + 7.

Example 1:
Input: n = 6, delay = 2, forget = 4
Output: 5

Explanation:
Day 1: A (1 person)
Day 2: A (1 person)
Day 3: A shares with B (2 people)
Day 4: A shares with C (3 people)
Day 5: A forgets; B shares with D (3 people)
Day 6: B shares with E, C shares with F (5 people)

A: 
A:
A,B: A -> B
A,B,C: A -> C
B,C: B -> D
B,C,D: B -> E, C -> F
B,C,D,E,F

n=0, [1,0,0,0,0,0]
n=1, [1,0,0,0,0,0]
n=2, [1,0,1,0,0,0]
n=3, [1,0,1,1,0,0]
n=4, [0,0,1,1,1,0]
n=5, [0,0,1,1,1,2]

1,1,2,3

n=0, [1,0,0,0,0,0]
n=1, [1,0,0,0,0,0]
n=2, [1,0,1,1,0,0]
n=3, [1,0,1,1,0,0]
n=4, [0,0,1,1,1,1]
n=5, [0,0,1,1,1,2]

Example 2:
Input: n = 4, delay = 1, forget = 3
Output: 6

Explanation:
Day 1: A
Day 2: A shares with B
Day 3: A, B share with C, D
Day 4: A forgets; B, C, D share with E, F, G

n=0, [1,0,0,0]
n=1, [1,1,1,0]
n=2, [1,1,2,2]
n=3, [0,1,2,2]

Constraints:
- 2 <= n <= 1000
- 1 <= delay < forget <= n
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        who_knows = 0
        for i in range(2, n + 1):
            if i > delay:
                who_knows = (who_knows + dp[i - delay]) % MOD
            if i > forget:
                who_knows = (who_knows - dp[i - forget] + MOD) % MOD
            dp[i] = who_knows

        answer = 0
        for i in range(n-forget+1, n+1):
            answer = (answer + dp[i]) % MOD
        return answer


if __name__ == "__main__":
    tests = [
        [6, 2, 4],
        [4, 1, 3],
    ]
    answers = [5, 6]

    tester = Tester(Solution().peopleAwareOfSecret)
    tester.test(tests, answers)
