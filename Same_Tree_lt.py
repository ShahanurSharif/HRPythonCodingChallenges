from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_preOrder(tree):

        return []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.dfs_preOrder(p)
        self.dfs_preOrder(q)

        return False



if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(p, q))