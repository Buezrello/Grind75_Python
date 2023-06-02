from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def diameter_calculating(node: TreeNode) -> int:
            if not node:
                return 0

            left = diameter_calculating(node.left)
            right = diameter_calculating(node.right)

            if left + right > self.diameter:
                self.diameter = left + right

            return max(left, right) + 1

        diameter_calculating(root)
        return self.diameter


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    print(sol.diameterOfBinaryTree(root))

    root = TreeNode(1)
    root.left = TreeNode(2)

    print(sol.diameterOfBinaryTree(root))