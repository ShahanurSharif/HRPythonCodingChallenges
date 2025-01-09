from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, arr=[]):
        if root is None:
            return

        arr.append(root.val)
        self.dfs(root.right, arr)
        return arr

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)


    sol = Solution()
    print(sol.rightSideView(p))