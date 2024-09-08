from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    """Leetcode ListNode data structure."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self) -> str:
        result = []
        node = self
        while node is not None:
            result.append(node.val)
            node = node.next
        return str(result)

    def __eq__(self, other: "ListNode") -> bool:
        node1 = self
        node2 = other

        while node1 is not None and node2 is not None and node1.val == node2.val:
            node1 = node1.next
            node2 = node2.next

        if node1 is None and node2 is None:
            return True

        if (node1 is None and node2 is not None) or (
            node1 is not None and node2 is None
        ):
            return False

        return node1.val == node2.val


def get_ListNode(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    node = head

    for i in range(1, len(nums)):
        node.next = ListNode(nums[i])
        node = node.next

    return head


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        result = []

        def traverse(node: Optional[TreeNode]):
            if node is None:
                return

            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(self)
        return str(result)


def get_TreeNode(nums: List[Optional[int]]) -> TreeNode:
    root = TreeNode(nums[0])
    root.left = TreeNode(nums[1])
    root.right = TreeNode(nums[2])

    nodes = [root.left, root.right]

    idx = 3
    while len(nodes) > 0:
        node = nodes.pop(0)
        if node is not None and idx < len(nums):
            node.left = TreeNode(nums[idx]) if nums[idx] else None
            idx += 1
            node.right = TreeNode(nums[idx]) if nums[idx] else None
            idx += 1

            nodes += [node.left, node.right]

    return root
