from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an integer array groups, where groups[i] represents the size of the ith group.
You are also given an integer array elements.

Your task is to assign one element to each group based on the following rules:
1. An element j can be assigned to a group i if groups[i] is divisible by elements[j].
2. If there are multiple elements that can be assigned, assign the element with the smallest index j.
3. If no element satisfies the condition for a group, assign -1 to that group.

Return an integer array assigned, where assigned[i] is the index of the element chosen for group i, or -1 if no suitable element exists.

Note: An element may be assigned to more than one group.

Example 1:
Input: groups = [8,4,3,2,4], elements = [4,2]
Output: [0,0,-1,1,0]

Explanation:
- elements[0] = 4 is assigned to groups 0, 1, and 4.
- elements[1] = 2 is assigned to group 3.
- Group 2 cannot be assigned any element.

Example 2:
Input: groups = [2,3,5,7], elements = [5,3,3]
Output: [-1,1,0,-1]

Explanation:
- elements[1] = 3 is assigned to group 1.
- elements[0] = 5 is assigned to group 2.
- Groups 0 and 3 cannot be assigned any element.

Example 3:
Input: groups = [10,21,30,41], elements = [2,1]
Output: [0,1,0,1]

Explanation:
- elements[0] = 2 is assigned to the groups with even values.
- elements[1] = 1 is assigned to the groups with odd values.

Constraints:
1. 1 <= groups.length <= 10^5
2. 1 <= elements.length <= 10^5
3. 1 <= groups[i] <= 10^5
4. 1 <= elements[i] <= 10^5
"""


class Solution:
    def assignElementsToGroups(
        self, groups: List[int], elements: List[int]
    ) -> List[int]:
        max_grp = max(groups)
        elem_map = {}
        for i, elem in enumerate(elements):
            if elem in elem_map:
                continue

            for el in range(elem, max_grp + 1, elem):
                if el not in elem_map:
                    elem_map[el] = i

        answer = [-1] * len(groups)
        for i, grp in enumerate(groups):
            if grp in elem_map:
                answer[i] = elem_map[grp]

        return answer


if __name__ == "__main__":
    tests = [
        [[8, 4, 3, 2, 4], [4, 2]],
        [[2, 3, 5, 7], [5, 3, 3]],
        [[10, 21, 30, 41], [2, 1]],
        [[2], [1, 2, 1, 1]],
        [
            generate_random_int_array(16**5, start_n=1, end_n=10**5),
            generate_random_int_array(16**5, start_n=1, end_n=10**5),
        ],
    ]
    answers = [[0, 0, -1, 1, 0], [-1, 1, 0, -1], [0, 1, 0, 1], [0], [-1]]

    tester = Tester(Solution().assignElementsToGroups)
    tester.test(tests, answers)
