from tester import Tester

"""
328. Odd Even Linked List
Medium

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 4, 5]],
        [[2, 1, 3, 5, 6, 4, 7]],
    ]
    answers = [
        [1, 3, 5, 2, 4],
        [2, 3, 6, 7, 1, 5, 4],
    ]

    tester = Tester(Solution().oddEvenList)
    tester.test(tests, answers)
