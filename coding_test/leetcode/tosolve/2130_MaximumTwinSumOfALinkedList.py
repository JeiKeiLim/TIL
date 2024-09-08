from tester import Tester

"""
2130. Maximum Twin Sum of a Linked List
Medium

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:

Input: head = [5,4,2,1]
Output: 6

Example 2:

Input: head = [4,2,2,3]
Output: 7

Example 3:

Input: head = [1,100000]
Output: 100001
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> int:
        pass


if __name__ == "__main__":
    tests = [
        [[5, 4, 2, 1]],
        [[4, 2, 2, 3]],
        [[1, 100000]],
    ]
    answers = [
        6,
        7,
        100001,
    ]

    tester = Tester(Solution().pairSum)
    tester.test(tests, answers)
