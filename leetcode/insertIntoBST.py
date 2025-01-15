# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        left_value = self.insertIntoBST(root.left, val)
        right_value = self.insertIntoBST(root.right, val)

        if val < left_value.val or val > right_value.val:
            return TreeNode(val)



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    insert_value = 5

    sol = Solution()
    value = sol.insertIntoBST(root, insert_value)
    print(value)