from tester import Tester

"""
There is a programming language with only four operations and one variable X:
- ++X and X++ increments the value of the variable X by 1.
- --X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

Example 1:
Input: operations = ["--X","X++","X++"]
Output: 1

Example 2:
Input: operations = ["++X","++X","X++"]
Output: 3

Example 3:
Input: operations = ["X++","++X","--X","X--"]
Output: 0

Constraints:
1 <= operations.length <= 100
operations[i] will be either "++X", "X++", "--X", or "X--".
"""


class Solution3:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if op[1] == "+" else -1 for op in operations)


class Solution2:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        answer = 0
        for op in operations:
            if op[1] == "+":
                answer += 1
            else:
                answer -= 1
        return answer


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        op_map = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1,
        }
        x = 0
        for operation in operations:
            x += op_map[operation]

        return x


if __name__ == "__main__":
    tests = [
        [["--X", "X++", "X++"]],
        [["++X", "++X", "X++"]],
        [["X++", "++X", "--X", "X--"]],
    ]
    answers = [1, 3, 0]

    tester = Tester(Solution3().finalValueAfterOperations)
    tester.test(tests, answers)
