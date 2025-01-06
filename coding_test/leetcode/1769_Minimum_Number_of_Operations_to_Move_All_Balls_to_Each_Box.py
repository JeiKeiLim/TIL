from tester import Tester

from typing import List
import random

"""
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty,
and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1.
Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls
to the ith box.

Example 1:
Input: boxes = "110"

110
0 1 3
1 0 0

Output: [1,1,3]
Explanation:
1. First box: Move one ball from the second box to the first box in one operation.
2. Second box: Move one ball from the first box to the second box in one operation.
3. Third box: Move one ball from the first box to the third box in two operations,
   and move one ball from the second box to the third box in one operation.

Example 2:
Input: boxes = "001011"
Output: [11,8,5,4,3,4]

001011
 0 0 0 1 2 4
11 8 5 3 1 0

Constraints:
1. n == boxes.length
2. 1 <= n <= 2000
3. boxes[i] is either '0' or '1'.
"""


class Solution:
    def minOperations2(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        n_box = 0
        total = 0
        for i in range(n):
            answer[i] += total
            if boxes[i] == "1":
                n_box += 1
            total += n_box

        n_box, total = 0, 0
        for i in range(n - 1, -1, -1):
            answer[i] += total
            if boxes[i] == "1":
                n_box += 1
            total += n_box

        return answer

    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        for i in range(n):
            local_sum = 0
            for j in range(n):
                if i == j or boxes[j] == "0":
                    continue
                local_sum += abs(j - i)
            answer[i] = local_sum
        return answer


if __name__ == "__main__":
    tests = [
        ["110"],
        ["001011"],
        ["".join([chr(random.randint(ord("0"), ord("1"))) for _ in range(10000)])],
    ]
    answers = [[1, 1, 3], [11, 8, 5, 4, 3, 4], [-1]]

    tester = Tester(Solution().minOperations2, verbose=0)
    tester.test(tests, answers)
