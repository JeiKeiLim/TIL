from tester import Tester

"""
2095. Delete the Middle Node of a Linked List
Medium

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing.

Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]

Example 3:

Input: head = [2,1]
Output: [2]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    # Helper function to create linked list from list and return head
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert linked list to list for easy comparison
    def linked_list_to_list(head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    tests = [
        [create_linked_list([1, 3, 4, 7, 1, 2, 6]), [1, 3, 4, 1, 2, 6]],
        [create_linked_list([1, 2, 3, 4]), [1, 2, 4]],
        [create_linked_list([2, 1]), [2]],
    ]

    # Expected answers
    answers = [[1, 3, 4, 1, 2, 6], [1, 2, 4], [2]]

    tester = Tester(Solution().deleteMiddle)
    tester.test(tests, answers)
