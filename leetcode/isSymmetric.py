from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs(self, root, left, right):
        pass

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = float('-inf')
        right = float('inf')
        return self.bfs(root, left, right)

if __name__ == '__main__':
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(2)

    solution = Solution()
    print(solution.isSymmetric(q))

