from tester import Tester

from typing import List
import random

import heapq

"""
There is a school that has classes of students and each class will be having a final exam.
You are given a 2D integer array classes, where classes[i] = [passi, totali].

You know beforehand that in the ith class, there are totali total students,
but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed
to pass the exam of any class they are assigned to.

You want to assign each of the extraStudents students to a class in a way that maximizes
the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam
divided by the total number of students of the class.

The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students.
Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation:
You can assign the two extra students to the first class.
The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

Example 2:
Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485

Constraints:
1 <= classes.length <= 10^5
classes[i].length == 2
1 <= passi <= totali <= 10^5
1 <= extraStudents <= 10^5
"""


class Solution:
    def maxAverageRatio2(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        O(max(n, k log n))
        """
        new_classes = [((x[0]/x[1])-((x[0]+1)/(x[1]+1)), x[0], x[1]) for x in classes]
        heapq.heapify(new_classes)

        for _ in range(extraStudents):
            x = heapq.heappop(new_classes)
            new_ratio = ((x[1]+1) / (x[2]+1)) - ((x[1]+2)/(x[2]+2))
            heapq.heappush(new_classes, (new_ratio, x[1]+1, x[2]+1))

        return sum([x[1] / x[2] for x in new_classes]) / len(new_classes)


    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        while extraStudents > 0:  # O(k n log n)
            classes.sort(
                key=lambda x: ((x[0] + 1) / (x[1] + 1)) - (x[0] / x[1]), reverse=True
            )

            classes[0][0] += 1
            classes[0][1] += 1

            extraStudents -= 1

        return sum([x[0] / x[1] for x in classes]) / len(classes)


if __name__ == "__main__":
    tests = [
        [[[1, 2], [3, 5], [2, 2]], 2],
        [[[2, 4], [3, 9], [4, 5], [2, 10]], 4],
        [
            [
                [x, random.randint(x, x + 10000)]
                for x in [random.randint(1, 10000) for _ in range(20000)]
            ],
            random.randint(1, 5000),
        ],
    ]
    answers = [0.78333, 0.53485, -1]

    tester = Tester(Solution().maxAverageRatio2, verbose=0)
    tester.test(tests, answers)
