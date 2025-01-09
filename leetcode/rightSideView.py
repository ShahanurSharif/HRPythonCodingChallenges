from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, level=0, arr=[]):
        if root is None:
            return
        if level == len(arr):
            arr.append(root.val)

        self.dfs(root.right, level+1, arr)
        self.dfs(root.left, level+1, arr)
        return arr

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.dfs(root, 0, result)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.left.left = TreeNode(4)
    p.left.left.left = TreeNode(5)
    p.right = TreeNode(3)

    sol = Solution()
    print(sol.rightSideView(p))


    p = TreeNode(1)
    # p.left = TreeNode(2)
    # p.left.left = TreeNode(4)
    # p.left.left.left = TreeNode(5)
    p.right = TreeNode(3)




    sol = Solution()
    print(sol.rightSideView(p))

