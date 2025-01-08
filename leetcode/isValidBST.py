# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], previous_value=None):
        # print('hello world')
        if root is None:
            return

        getLeftNode = self.dfs(root.left, previous_value)
        getRightNode = self.dfs(root.right, previous_value)
        print(root.val)


        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hello world')
        self.dfs(root)
        return True

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)

    solution = Solution()
    print(solution.isValidBST(node))