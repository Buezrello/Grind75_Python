from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height_balance(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    left_height = height_balance(node.left)
    if left_height == -1:
        return -1

    right_height = height_balance(node.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        return height_balance(root) >= 0

