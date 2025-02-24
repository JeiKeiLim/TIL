from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    """Leetcode ListNode data structure."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self) -> str:
        node_map = {}

        result = []
        node = self
        while node is not None:
            if node.val not in node_map:
                node_map[node.val] = [node]
            elif node in node_map[node.val]:
                result.append(f"(Cycle -> {node.val})")
                break
            else:
                node_map[node.val].append(node)

            result.append(f"{node.val}")
            node = node.next
        return ", ".join(result)


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

    def __eq__(self, value: "TreeNode") -> bool:
        return str(self) == str(value)

    def __len__(self) -> int:
        length = [0]

        def traverse(node: Optional[TreeNode]):
            if node is None:
                return

            length[0] += 1

            traverse(node.left)
            traverse(node.right)

        traverse(self)
        return length[0]

    def get_preorder(self) -> List[int]:
        result = []
        queue = [self]
        while queue:
            node = queue.pop()
            if node is None:
                continue
            result.append(node.val)

            queue.append(node.right)
            queue.append(node.left)
        return result

    def get_postorder(self) -> List[int]:
        result = []
        queue = [self]
        while queue:
            node = queue.pop()
            if node is None:
                continue
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        return result[::-1]


def get_TreeNode(nums: List[Optional[int]]) -> TreeNode:
    root = TreeNode(nums[0])
    if len(nums) == 1:
        return root

    root.left = TreeNode(nums[1])
    if len(nums) == 2:
        return root

    root.right = TreeNode(nums[2])
    if len(nums) == 3:
        return root

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
