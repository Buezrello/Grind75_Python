# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        return right
