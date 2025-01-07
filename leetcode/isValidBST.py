# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], previous_value=None):
        if root is None:
            return root

        getLeftNode = self.dfs(root.left, previous_value)
        getRightNode = self.dfs(root.right, previous_value)

        print(getLeftNode, getRightNode, root.val)

        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root)

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)