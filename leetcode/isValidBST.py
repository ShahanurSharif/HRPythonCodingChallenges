# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return root

        getLeftNode = self.dfs(root.left)
        getRightNode = self.dfs(root.right)

        print(getLeftNode, getRightNode)

        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root)

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)